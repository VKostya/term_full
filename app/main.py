from fastapi import FastAPI
from sqlalchemy.orm import Session
from db.db_engine import engine
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from api.terms import term_router
from api.links import link_router
from app.glossary import glossary_router
from app.mind_map import mindmap_router
from db.models import Base
from config import config
import uvicorn 

app = FastAPI()
app.include_router(term_router, prefix="/api")
app.include_router(link_router, prefix="/api")
app.include_router(glossary_router)
app.include_router(mindmap_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app, host=config.HOST, port=config.PORT)