from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey, String
from .Ticket import Ticket
from .User import User
from .dates import datetime_to_str
import logging

Base = declarative_base()


class Post(Base):

    __tablename__ = "post"
    id = Column(Integer, primary_key=True, autoincrement=True)
    ticket_id = Column(Integer, ForeignKey(Ticket.id))
    author_id = Column(Integer, ForeignKey(User.id))
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    status_change=Column(String(50))
    content = Column(Text, nullable=False)

    def __init__(self, ticket, author, content, id=None, status_change=None):

        self.ticket_id = ticket
        self.author_id = author
        self.content = content
        self.status_change = status_change
        if id:
            self.id = id


    def to_json(self):

        result = { "ticket_id": self.ticket_id, "author_id": self.author_id, "timestamp": datetime_to_str(self.timestamp),"id": self.id, "content": self.content, 'status_change': self.status_change}

        return result

    @staticmethod
    def from_json(json_data):

        if 'id' in json_data:
            result = Post(json_data['ticket_id'], json_data['author_id'], json_data['content'], json_data['id'], json_data['status_change'])
        else:
            logging.info(json_data)
            result = Post(json_data['ticket_id'], json_data['author_id'], json_data['content'], status_change=json_data['status_change'])

        return result
