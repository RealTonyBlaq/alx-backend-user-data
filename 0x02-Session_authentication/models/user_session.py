#!/usr/bin/env python3
""" UserSession Module """

from models.base import Base


class UserSession(Base):
    """ Defining the UserSession Auth system """

    def __init__(self, *args: list, **kwargs: dict):
        """
        Initailize the attributes:
        
        """
