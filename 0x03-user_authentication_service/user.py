#!/usr/bin/env python3
""" User Model """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User:
    """ Defining the class User """
    __tablename__ = "users"
    id = Column('id', Integer, primary_key=True, nullable=False)
    email = Column('email', String(60), nullable=False)
    hashed_password = Column('hashed_password', )
    
