from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime
from .dates import datetime_to_str, str_to_datetime


Base = declarative_base()


class Ticket(Base):

    __tablename__ = "ticket"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    status = Column(String(30), nullable=False)
    deadline = Column(DateTime(timezone=True))

    def __init__(self, title, deadline, status='new', id=None):

        self.title = title
        self.deadline = deadline
        self.status = status
        if id:
            self.id = id

    def to_json(self):

        result = {"title": self.title, "status": self.status, "deadline": datetime_to_str(self.deadline),"id": self.id }

        return result

    @staticmethod
    def from_json(json_data):

        if 'id' in json_data:
            result = Ticket(json_data['title'], str_to_datetime(json_data['deadline']), json_data['status'], json_data['id'])
        else:
            result = Ticket(json_data['title'], str_to_datetime(json_data['deadline']), json_data['status'])

        return result

