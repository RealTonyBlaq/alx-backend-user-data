#!/usr/bin/env python3
""" User Model """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


class User:
    """ Defining the class User """
    __tablename__ = "users"
