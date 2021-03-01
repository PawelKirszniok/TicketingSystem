from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey

Base = declarative_base()


class Post(Base):

    __tablename__ = "post"
    id = Column(Integer, primary_key=True, autoincrement=True)
    ticket_id = Column(Integer, ForeignKey("ticket.id"))
    author_id = Column(Integer, ForeignKey("user.id"))
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    content = Column(Text, nullable=False)

    def __init__(self, ticket, author, content):

        self.ticket_id = ticket
        self.author_id = author
        self.content = content
