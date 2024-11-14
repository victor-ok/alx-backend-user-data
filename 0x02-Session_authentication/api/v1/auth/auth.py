#!/usr/bin/env python3
"""
Authentication Module
"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """Authentication class implementation"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Later implementation
        """
        if not path or not excluded_paths:
            return True
        if len(excluded_paths) < 1:
            return True
        for p in excluded_paths:
            if self.strip_slash(p) == self.strip_slash(path):
                return False
            if self.asterik_handler(p, path):
                return False
        return True

    @staticmethod
    def strip_slash(data: str) -> str:
        """
        Remove a forward slash character at the end of the string
        Arg:
         data: the string to check and strip
        """
        if data.endswith("/"):
            return data[:-1]
        return data

    @staticmethod
    def asterik_handler(link: str, path: str) -> bool:
        """
        Compare the path with a link ending with *
        Args:
            link: the link
            path: the path
        """
        if link.endswith("*"):
            link = link.strip("*")
            if path.startswith(link):
                return True

    def authorization_header(self, request=None) -> str:
        """
        recieves request and retrrives header information
        Arg:
            request: Flask request object
        """
        if request:
            header = request.headers.get("Authorization")
            return header
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        returns current user if exists
        Arg:
            request: Flask request object
        """
        return None

    def session_cookie(self, request=None):
        """ Returns request cookie value """
        if request is None:
            return None
        cookie = getenv('SESSION_NAME')
        return request.cookies.get(cookie)
