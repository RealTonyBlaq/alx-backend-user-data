#!/usr/bin/env python3
""" User Model """

from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User:
    """ Defining the class User """
    __tab
    id = Column('id', Integer, primary_key=True, nullable=False)
    email = Column('email', String(60), nullable=False)
    hashed_password = Column('hashed_password', String(256), nullable=False)
    session_id = Column('session_id', String(256))
    reset_token = Column('reset_token', String(256))
