#!/usr/bin/env python3
"""
Basic Auth module
"""

from api.v1.auth.auth import Auth
from typing import TypeVar, List
from models.user import User
import base64
import binascii


class BasicAuth(Auth):
    """
    class BasicAuth
    """

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        returns the base64 part of the authorization
        header for a Basic auth
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        header_array = authorization_header.split(" ")
        if header_array[0] != "Basic":
            return None
        else:
            return header_array[1]

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """
        returnz decoded val of Base64 string
        base64_authorization_header
        """
        bs64_auth_header = base64_authorization_header
        if bs64_auth_header and isinstance(bs64_auth_header, str):
            try:
                encode = bs64_auth_header.encode('utf-8')
                base = base64.b64encode(encode)
                return base.decode('utf-8')
            except binascii.Error:
                return None

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        """
        returns the user emal and password from the Base64 decoded val
        """
        decoded = decoded_base64_authorization_header
        if (decoded and isinstance(decoded, str) and ":" in decoded):
            req = decoded.split(":", 1)
            return (req[0], req[1])
        return (None, None)


    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        returns the User instance based on his email and password.
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            users = User.search({'email': user_email})
            if not users or users == []:
                return None
            for u in users:
                if u.is_valid_password(user_pwd):
                    return u
            return None
        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        overloads Auth and retrieves the User instance for a request:
        """
        Auth_header = self.authorization_header(request)
        if Auth_header is not None:
            token = self.extract_base64_authorization_header(Auth_header)
            if token is not None:
                decoded = self.decode_base64_authorization_header(token)
                if decoded is not None:
                    email, pword = self.extract_user_credentials(decoded)
                    if email is not None:
                        return self.user_object_from_credentials(email, pword)
