from sqlalchemy import Column, String, Boolean, Integer, ForeignKey, JSON
from sqlalchemy.orm import relationship
from app.db.base import Base


class VPNConnectionModel(Base):
    __tablename__ = "vpn_connections"

    connection_id = Column(String, primary_key=True, index=True)

    state = Column(String, default="down")  # up/down

    # # relationships
    # local_addrs = relationship("VPNLocalAddr", cascade="all, delete-orphan")
    # remote_addrs = relationship("VPNRemoteAddr", cascade="all, delete-orphan")

    # local_auth = relationship("VPNAuth", uselist=False, cascade="all, delete-orphan")
    # remote_auth = relationship("VPNAuth", uselist=False, cascade="all, delete-orphan")

    # children = relationship("VPNChildSA", cascade="all, delete-orphan")
    config = Column(JSON)



# class VPNLocalAddr(Base):
#     __tablename__ = "vpn_local_addrs"

#     id = Column(Integer, primary_key=True)
#     connection_id = Column(String, ForeignKey("vpn_connections.connection_id"))

#     address = Column(String)

# class VPNRemoteAddr(Base):
#     __tablename__ = "vpn_remote_addrs"

#     id = Column(Integer, primary_key=True)
#     connection_id = Column(String, ForeignKey("vpn_connections.connection_id"))

#     address = Column(String)

# class VPNAuth(Base):
#     __tablename__ = "vpn_auth"

#     id = Column(Integer, primary_key=True)
#     connection_id = Column(String, ForeignKey("vpn_connections.connection_id"))

#     side = Column(String)  # "local" or "remote"
#     auth_method = Column(String)  # "psk" or "cert"

#     # PSK
#     psk_ref = Column(String, nullable=True)

#     # certificate auth
#     cert_ref = Column(String, nullable=True)
#     key_ref = Column(String, nullable=True)

# class VPNChildSA(Base):
#     __tablename__ = "vpn_child_sa"

#     id = Column(Integer, primary_key=True)
#     connection_id = Column(String, ForeignKey("vpn_connections.connection_id"))

#     name = Column(String)

#     mode = Column(String, default="tunnel")
#     start_action = Column(String, default="trap")

#     local_ts = Column(String)   # store as CSV or JSON string
#     remote_ts = Column(String)

# class VPNProposal(Base):
#     __tablename__ = "vpn_proposals"

#     id = Column(Integer, primary_key=True)
#     connection_id = Column(String, ForeignKey("vpn_connections.connection_id"))

#     proposal = Column(String)  # e.g. aes256-sha256-modp2048