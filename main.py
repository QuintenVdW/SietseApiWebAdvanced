from fastapi import FastAPI, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .routes import r0944736_endpoints  # Update import statement

import os


# Create a FastAPI app instance
app = FastAPI()

# Include the router from endpoints.py
app.include_router(r0944736_endpoints.router)


# Create a SQLAlchemy engine
SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL")
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get a database session for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Define your routes here
@app.get("/")
def root(db=Depends(get_db)):
    # Use the database session (db) to interact with your models
    # Example: query the database using your models
    # result = db.query(YourModel).all()
    return {"message": "Hello, World!"}