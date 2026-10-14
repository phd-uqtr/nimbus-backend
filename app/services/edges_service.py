from app.models.edge import Edge
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from app.schemas.edge import CreateEdgeRequest, CreateEdgeResponse
def register_edge(db, edge_data: CreateEdgeRequest):
    try:
        existing_edge = db.query(Edge).filter(Edge.id == edge_data.id).first()
        if existing_edge:
            raise HTTPException(
                status_code=409,
                detail=f"Edge {edge_data.id} already exists"
            )
        edge_db_data = {
            "id": edge_data.id,
            "serial_number": edge_data.serial_number,
            "mgmt_ip_address": edge_data.mgmt_ip_address,
            "cpu_capacity": edge_data.cpu_capacity,
            "memory_capacity": edge_data.memory_capacity,
            "disk_capacity": edge_data.disk_capacity,
            "edge_location": edge_data.edge_location
        }
        print(edge_data)
        edge = Edge(**edge_db_data)
        print(edge)
        db.add(edge)
        db.flush()   # ensures ID is written before commit
        db.commit()
        db.refresh(edge)
        return {
            "status": "registered",
            "edge_id": edge.id
        }
    except HTTPException as e:
        print(e)

        return {
            "status": "error",
            "message": e.detail
        }

    except SQLAlchemyError as e:
        db.rollback()
        print(e)
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {str(e)}"
        )

    except Exception as e:
        print(e)
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Unexpected error: {str(e)}"
        )


def list_edges(db):
    return db.query(Edge).all()