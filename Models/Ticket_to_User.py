from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class Ticket_to_User(Base):

    __tablename__ = "ticket_to_user"
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    ticket_id = Column(Integer, ForeignKey('ticket.id'),primary_key=True)
    user_role = Column(String, primary_key=True)

    def __init__(self, user, ticket, role):
        self.user_id = user
        self.ticket_id = ticket
        self.user_role = role
