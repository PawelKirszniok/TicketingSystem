from configparser import ConfigParser
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from.Models.User import User
from.Models.Ticket import Ticket
from.Models.Post import Post
from.Models.Ticket_to_User import Ticket_to_User


class DatabaseService:

    def __init__(self):

        config_object = ConfigParser()
        config_object.read("config.ini")

        dbConfig = config_object['DATABASECONFIG']
        login_string = f"{dbConfig['prefix']}://{dbConfig['user']}:{dbConfig['password']}@{dbConfig['host']}/{dbConfig['dbname']}"

        engine = create_engine(login_string, pool_pre_ping=True)
        self.session = sessionmaker(bind=engine)()

    def get_user(self, id: int) -> User:
        try:
            search = self.session.query(User).filter_by(id=id).all()
        except SQLAlchemyError:
            self.session.rollback()
            return None

        if len(search):
            return search[0]
        else:
            return None

    def get_ticket(self, id: int) -> Ticket:
        try:
            search = self.session.query(Ticket).filter_by(id=id).all()
        except SQLAlchemyError:
            self.session.rollback()
            return None

        if len(search):
            return search[0]
        else:
            return None

    def get_post(self, id: int) -> Post:
        try:
            search = self.session.query(Post).filter_by(id=id).all()
        except SQLAlchemyError:
            self.session.rollback()
            return None

        if len(search):
            return search[0]
        else:
            return None
