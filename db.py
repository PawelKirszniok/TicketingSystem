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

    def search_ticket(self, user: int, role: str = None) -> list[Ticket]:

        if role:
            try:
                search = self.session.query(Ticket_to_User).filer_by(user_id=user, user_role=role)
            except SQLAlchemyError:
                self.session.rollback()
                return None

        else:
            try:
                search = self.session.query(Ticket_to_User).filer_by(user_id=user)
            except SQLAlchemyError:
                self.session.rollback()
                return None

        result = []
        for item in search:
            if item.ticket_id not in result:
                result.append(item.ticket_id)

        search_result = []
        for id in result:
            tmp = self.get_ticket(id)
            if tmp:
                search_result.append(tmp)

            # here should be some extra error handling or logging if we got a none result

        return search_result

    def search_user(self, ticket: int) -> list[User]:

        try:
            search = self.session.query(Ticket_to_User).filer_by(ticket_id=ticket)
        except SQLAlchemyError:
            self.session.rollback()
            return None

        result = []
        for item in search:
            if item.user_id not in result:
                result.append(item.user_id)

        search_result = []
        for id in result:
            tmp = self.get_user(id)
            if tmp:
                search_result.append(tmp)

            # here should be some extra error handling or logging if we got a none result

        return search_result

    def search_post(self, user: int = None, ticket: int = None) -> list[Post]:
        """
        Get a list of posts of a particular user or belonging to a ticket. Use only one of the modes at the time.
        """
        if ticket and user:
            return None

        if ticket:
            try:
                search = self.session.query(Post).filer_by(ticket_id=ticket)
            except SQLAlchemyError:
                self.session.rollback()
                return None

        else:
            try:
                search = self.session.query(Post).filer_by(author_id=user)
            except SQLAlchemyError:
                self.session.rollback()
                return None

        return search

    def save_user(self, user: User):

        try:
            self.session.add(user)
            self.session.commit()
        except SQLAlchemyError:
            self.session.rollback()
            raise

    def save_ticket(self, ticket: Ticket):

        try:
            self.session.add(ticket)
            self.session.commit()
        except SQLAlchemyError:
            self.session.rollback()
            raise

    def save_post(self, post: Post):

        try:
            self.session.add(post)
            self.session.commit()
        except SQLAlchemyError:
            self.session.rollback()
            raise

    def save_relationship(self, user_id, ticket_id, role):

        rel = Ticket_to_User(user_id, ticket_id, role)

        try:
            self.session.add(rel)
            self.session.commit()

        except SQLAlchemyError:
            self.session.rollback()
            raise

