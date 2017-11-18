from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Boolean


Base = declarative_base()


class Location(Base):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True, autoincrement=True)
    time = Column(Integer)
    lat = Column(Float)
    lang = Column(Float)
    user_id = Column(String)
    address = Column(String)
    active = Column(Boolean)
