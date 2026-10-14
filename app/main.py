from fastapi import FastAPI
from app.api.routes import edges, vpn
from app.db.init import init_db
from fastapi.middleware.cors import CORSMiddleware

init_db()
app = FastAPI(title="Edge Orchestrator")

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # Allows specific origins
    allow_credentials=True,           # Allows cookies and auth headers
    allow_methods=["*"],              # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],              # Allows all headers
)
app.include_router(edges.router, prefix="/edges", tags=["edges"])
app.include_router(vpn.router, prefix="/vpn", tags=["vpn"])
