from .meta import Base
import datetime

from sqlalchemy import (Table,
    Column,
    Integer,
    Unicode,
    UnicodeText,
    DateTime,
    Float,
    String,
    ForeignKey)
from sqlalchemy.schema import UniqueConstraint
from passlib.apps import custom_app_context


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(Unicode(255), nullable=False)
    last_name = Column(Unicode(255), nullable=False)
    email = Column(Unicode(255), nullable=False, unique = True)
    username = Column(Unicode(255), nullable=True, unique=True)
    password = Column(Unicode(255), nullable=False)


    def set_password(self, password):
        self.password = custom_app_context.encrypt(password)

        
    
