#!/usr/bin/env python3
""" Authentication module
"""

from flask import request


class Auth:
    """
    Auth class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        To be inmplemented
        """
        if not path or not excluded_paths:
            return True
        
        return True

    def authorization_header(self, request=None) -> str:
        """
        retrives and receives request headers
        Arg:
            request Flask request obj
        """
        if request:
            header = header.headers.get("Authorization")
            return header
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        """
        return None

