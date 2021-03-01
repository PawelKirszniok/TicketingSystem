from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship

Base = declarative_base()


class Ticket(Base):

    __tablename__ = "ticket"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    posts = relationship("Post")
    users = relationship("Ticket_to_user")
    status = Column(String, nullable=False)
    deadline = Column(DateTime(timezone=True))


    def __init__(self, title, deadline):

        self.title = title
        self.deadline = deadline
        self.status = 'new'