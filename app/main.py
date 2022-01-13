
from fastapi import FastAPI
from . import models
from .database import engine
from .routers import posts, users, auth, vote
from .config import Settings
from fastapi.middleware.cors import CORSMiddleware

# this below statement is responsible for creating the database using sqlalchemy but as we are using alembic its not necessary
#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")  
async def root():
    return {"message": "Hello World welcome to my fast api"}

