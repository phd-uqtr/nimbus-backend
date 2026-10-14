from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.vpn import VPNConnection
from app.db.session import get_db
from app.models.vpn import VPNConnectionModel
from app.pubsub.redis import publish_event

router = APIRouter()


@router.get("/connections")
def get_vpn(db: Session = Depends(get_db)):
    vpns = db.query(VPNConnectionModel).all()
    return vpns


@router.post("/connections")
def create_vpn(conn: VPNConnection, db: Session = Depends(get_db)):
    print(conn)
    existing = db.query(VPNConnectionModel).filter(
        VPNConnectionModel.connection_id == conn.connection_id
    ).first()

    if existing:
        raise HTTPException(status_code=409, detail="Connection already exists")

    print(conn.model_dump())
    vpn = VPNConnectionModel(**conn.model_dump())
    db.add(vpn)
    db.commit()
    db.refresh(vpn)

    publish_event("vpn-events", {"type": "vpn.create", "data": conn.model_dump()})

    return {"status": "created", "connection_id": vpn.connection_id}



@router.get("/connections/{connection_id}")
def get_vpn(connection_id: str, db: Session = Depends(get_db)):
    vpn = db.query(VPNConnectionModel).filter(
        VPNConnectionModel.connection_id == connection_id
    ).first()

    if not vpn:
        raise HTTPException(status_code=404, detail="Not found")

    return vpn


@router.delete("/connections/{connection_id}")
def delete_vpn(connection_id: str, db: Session = Depends(get_db)):
    vpn = db.query(VPNConnectionModel).filter(connection_id == VPNConnectionModel.connection_id).first()
    if not vpn:
        raise HTTPException(status_code=404, detail="No VPN profile found") 

    db.delete(vpn)
    db.commit()
    publish_event("vpn-deleted", {"connection_id": connection_id})

    return {"status": "deleted", "connection_id": connection_id}