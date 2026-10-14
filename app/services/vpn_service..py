from fastapi import HTTPException
from app.schemas.vpn import VPNConnection
from app.models.vpn import VPNModel

def create_vpn(db, conn: VPNConnection):
    existing = db.query(VPNModel).filter(
        VPNModel.connection_id == conn.connection_id
    ).first()

    if existing:
        raise HTTPException(status_code=409, detail="Connection already exists")

    vpn = VPNModel(**conn.model_dump())
    db.add(vpn)
    db.commit()
    db.refresh(vpn)

    # publish_vpn_event("created", vpn.connection_id)

    return {"status": "created", "connection_id": vpn.connection_id}

def get_vpn(db, connection_id: str):
    vpn = db.query(VPNModel).filter(
        VPNModel.connection_id == connection_id
    ).first()

    if not vpn:
        raise HTTPException(status_code=404, detail="Not found")

    return vpn