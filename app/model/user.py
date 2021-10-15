from sqlalchemy import (
    Column,
    String,
    Integer,
    Date
)

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True)
    username = Column(Integer)
    firstname = Column(String)
    lastname = Column(Date)
