from configparser import ConfigParser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models.User import User
from Models.Ticket import Ticket
from Models.Post import Post
from Models.Ticket_to_User import Ticket_to_User
from exceptions import exception_handler


class DatabaseService:

    def __init__(self):

        config_object = ConfigParser()
        config_object.read("TicketingBackground/TicketingSystem/config.ini")

        dbConfig = config_object['DATABASECONFIG']
        login_string = f"{dbConfig['prefix']}://{dbConfig['user']}:{dbConfig['password']}@{dbConfig['host']}/{dbConfig['dbname']}?charset=utf8"

        engine = create_engine(login_string, pool_pre_ping=True)

        self.session = sessionmaker(bind=engine)()

    @exception_handler
    def get_user(self, id: int) -> User:

        search = self.session.query(User).filter_by(id=id).all()

        if len(search):
            return search[0]
        else:
            return None

    @exception_handler
    def get_ticket(self, id: int) -> Ticket:

        search = self.session.query(Ticket).filter_by(id=id).all()

        if len(search):
            return search[0]
        else:
            return None

    @exception_handler
    def get_post(self, id: int) -> Post:

        search = self.session.query(Post).filter_by(id=id).all()

        if len(search):
            return search[0]
        else:
            return None

    @exception_handler
    def search_ticket(self, user: int, role: str = None) -> list:

        if role:
            search = self.session.query(Ticket_to_User).filter_by(user_id=user, user_role=role)

        else:
            search = self.session.query(Ticket_to_User).filter_by(user_id=user)

        result = []
        for item in search:
            if item.ticket_id not in result:
                result.append((item.ticket_id, item.user_role))

        search_result = []
        for id, role in result:
            tmp = self.get_ticket(id)
            if tmp:
                search_result.append((tmp,role))

        return search_result

    @exception_handler
    def search_ticket_ordered_by_role(self, user: int, role: str = None) -> list:

        if role:
            search = self.session.query(Ticket_to_User).filter_by(user_id=user, user_role=role).order_by(Ticket_to_User.user_role.asc())

        else:
            search = self.session.query(Ticket_to_User).filter_by(user_id=user).order_by(Ticket_to_User.user_role.asc())

        result = []
        for item in search:
            if item.ticket_id not in result:
                result.append((item.ticket_id, item.user_role))

        search_result = []
        for id, role in result:
            tmp = self.get_ticket(id)
            if tmp:
                search_result.append((tmp,role))

        return search_result

    @exception_handler
    def search_user(self, ticket: int) -> list:

        search = self.session.query(Ticket_to_User).filter_by(ticket_id=ticket)

        result = []
        for item in search:
            if item.user_id not in result:
                result.append((item.user_id, item.role))

        search_result = []
        for id in result:
            tmp = self.get_user(id[0])
            if tmp:
                search_result.append((tmp, id[1]))

        return search_result

    @exception_handler
    def validate_user(self, password, login: str = None, email: str = None) -> (int, bool):

        user_id = None
        valid_password = False
        if login:
            search = self.session.query(User).filter_by(login=login).all()
            if len(search):
                user_id = search[0].id
                if search[0].password == password:
                    valid_password = True
                    return user_id, valid_password

        if email:
            search = self.session.query(User).filter_by(email=email).all()
            if len(search):
                user_id = search[0].id
                if search[0].password == password:
                    valid_password = True
                    return user_id, valid_password

        return user_id, valid_password

    @exception_handler
    def str_search_user(self, text: str) -> list:

        search_term = '%'+ text + '%'

        search = self.session.query(User).filter(User.name.like(search_term)).all()
        search += self.session.query(User).filter(User.email.like(search_term)).all()
        search += self.session.query(User).filter(User.position.like(search_term)).all()

        if len(search):
            return search[0]
        else:
            return None

    @exception_handler
    def search_post(self, ticket: int ) -> list:

        search = self.session.query(Post).filter_by(ticket_id=ticket).order_by(Post.timestamp.asc())


        return search

    @exception_handler
    def save_user(self, user: User):

        self.session.add(user)
        self.session.commit()

    @exception_handler
    def save_ticket(self, ticket: Ticket) -> int:

        self.session.add(ticket)
        self.session.commit()

        return ticket.id

    @exception_handler
    def save_post(self, post: Post):

        self.session.add(post)
        self.session.commit()

    @exception_handler
    def save_relationship(self, user_id, ticket_id, role):

        rel = Ticket_to_User(user_id, ticket_id, role)

        self.session.add(rel)
        self.session.commit()

    @exception_handler
    def update(self):

        self.session.commit()

        return ticket.id

