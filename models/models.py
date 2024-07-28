from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import BigInteger
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

from data.config import DATABASE_URL



Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(BigInteger, primary_key=True, unique=True)
    name = Column(String)
    username = Column(String, nullable=True)
    
class Channel(Base):
    __tablename__ = "channels"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    channel_id = Column(BigInteger)
    name = Column(String)
    link = Column(String, nullable=True)
    
    
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

session = sessionmaker(bind=engine)()
