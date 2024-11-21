#!/usr/bin/env python3
"""
User Module
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer


Base = declarative_base()


class User(Base):
    """
    User Model
    Attrs:
        id: User Id
        email: Email address of the user
        hashed_password: User's hashed password
        session_id: session ID shared between requests
        reset_token: token to refresh sessions
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    email = Column(String(250), nullable=False, unique=True)
    hashed_password = Column(String(250), nullable=False, unique=True)
    session_id = Column(String(250), unique=True)
    reset_token = Column(String(250), unique=True)

    def __repr__(self):
        """
        String Rep
        """
        return f"User: id={self.id}"
