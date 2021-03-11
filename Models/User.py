from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):

    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    name = Column(String(100), nullable=False)
    picture = Column(String(100), nullable=False, default='default.jpg')
    position = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    posts = relationship("post")
    tickets = relationship("ticket_to_user")

    def __init__(self, login, password, name, position, email, picture='default.jpg'):
        self.login = login
        self.password = password
        self.name = name
        self.position = position
        self.email = email
        self.picture = picture




