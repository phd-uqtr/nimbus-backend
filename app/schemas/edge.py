from pydantic import BaseModel

class CreateEdgeRequest(BaseModel):
    id: str
    serial_number: str
    mgmt_ip_address: str
    cpu_capacity: int
    memory_capacity: int
    disk_capacity: int
    edge_location: str

class CreateEdgeResponse(CreateEdgeRequest):
    is_up: bool
    is_provisioned: bool