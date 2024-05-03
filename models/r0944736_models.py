from sqlalchemy import Column, Integer, String
from ..database import Base

class ExampleModel(Base):
    tablename = "community"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    Description = Column(String, index=True)