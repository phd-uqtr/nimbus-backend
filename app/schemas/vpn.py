from pydantic import BaseModel
from typing import List, Literal, Optional


class AuthMethod(BaseModel):
    auth_method: Literal["psk"]
    psk: Optional[str] = None


# child security association is the part of the VPN
# that actually carries the data traffic
# the ike sa negotiates and controls the connection, however child sa carries out the encrypted data traffic

class ChildSA(BaseModel):
    name: str
    local_ts: List[str] # local traffic selectors
    remote_ts: List[str] # remote traffic selectors
    mode: Literal["tunnel"]
    start_action: Literal["trap", "start"]


class VPNConfig(BaseModel):
    local_addrs: List[str]
    remote_addrs: List[str]

    local_auth: AuthMethod
    remote_auth: AuthMethod

    children: List[ChildSA]

    version: Literal["2"]
    proposals: List[str]


class VPNConnection(BaseModel):
    connection_id: str
    config: VPNConfig
