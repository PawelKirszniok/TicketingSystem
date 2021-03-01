from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Text, DateTime
from sqlalchemy.orm import relationship

Base = declarative_base()


class Ticket(Base):

    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(Text)
    posts = relationship("Post")
    deadline = Column(DateTime)