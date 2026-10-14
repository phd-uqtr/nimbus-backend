from sqlalchemy import Column, String, Integer, Boolean
from app.db.base import Base

class Edge(Base):
    __tablename__ = "edges"

    id = Column(String, primary_key=True)
    serial_number = Column(String, unique=True)
    mgmt_ip_address = Column(String)
    vpn_ip_address = Column(String)
    cpu_capacity = Column(Integer)
    memory_capacity = Column(Integer)
    disk_capacity = Column(Integer)
    edge_location = Column(String)
    is_up = Column(Boolean, default=False)
    is_provisioned = Column(Boolean, default=False)
