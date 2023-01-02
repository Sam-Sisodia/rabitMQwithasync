from database import Base
from sqlalchemy import Column,String,Integer


class message(Base):
    __tablename__ = "Message"
    id = Column(Integer,primary_key = True,index=True)
    topic = Column(String)
