from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from .Ticket import Ticket
from .User import User

Base = declarative_base()


class Post(Base):

    __tablename__ = "post"
    id = Column(Integer, primary_key=True, autoincrement=True)
    ticket_id = Column(Integer, ForeignKey(Ticket.id))
    author_id = Column(Integer, ForeignKey(User.id))
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    content = Column(Text, nullable=False)

    def __init__(self, ticket, author, content, id=None):

        self.ticket_id = ticket
        self.author_id = author
        self.content = content
        if id:
            self.id = id

    def to_json(self):

        result = f' "ticket_id": "{self.ticket_id}", "author_id": "{self.author_id}", "timestamp": "{self.timestamp}", ' \
                 f'"id": "{self.id}", "content": "{self.content}"'

        return '{' + result + '}'

    @staticmethod
    def from_json(json_data):

        if 'id' in json_data:
            result = Post(json_data['ticket_id'], json_data['author_id'], json_data['content'], json_data['id'])
        else:
            result = Post(json_data['ticket_id'], json_data['author_id'], json_data['content'])

        return result
