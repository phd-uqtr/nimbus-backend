from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.edge import CreateEdgeRequest
from app.models.edge import Edge
from app.services.edges_service import register_edge, list_edges
from app.db.session import get_db

router = APIRouter()

@router.post("/register")
def register(node: CreateEdgeRequest, db: Session = Depends(get_db)):
    return register_edge(db, node)

@router.get("/")
def list_nodes(db: Session = Depends(get_db)):
    return list_edges(db)