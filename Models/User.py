from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
import json

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

    def __init__(self, login, password, name, position, email, picture='default.jpg'):
        self.login = login
        self.password = password
        self.name = name
        self.position = position
        self.email = email
        self.picture = picture

    def to_json(self):

        result = f' "login": "{self.login}", "password": "{self.password}", "name": "{self.name}", ' \
                 f'"position": "{self.position}", "email": "{self.email}", "picture": "{self.picture}"'

        return '{' + result + '}'

    @staticmethod
    def from_json(json_data):

        dict_data = json_data

        result = User(dict_data['login'], dict_data['password'], dict_data['name'],dict_data['position'],
                      dict_data['email'], dict_data['picture'])

        return result






