from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):

    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String, nullable=False)
    password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    picture = Column(String, nullable=False, default='default.jpg')
    position = Column(String, nullable=False)
    email = Column(String, nullable=False)
    posts = relationship("Post")
    tickets = relationship("Ticket_to_user")

    def __init__(self, login, password, name, position, email, picture='default.jpg'):
        self.login = login
        self.password = password
        self.name = name
        self.position = position
        self.email = email
        self.picture = picture




