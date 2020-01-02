import hashlib
import os
import base64
import bcrypt
import uuid


class PasswordHelper:

    def get_hash(self, plain):
        return hashlib.sha512(plain).digest()

    def get_salt(self):
        return base64.b64encode(os.urandom(20)).encode('utf-8')
        # return bcrypt.gensalt()
        return uuid.uuid4().bytes

    def validate_password(self, plain, salt, expected):
        return self.get_hash(bytes(plain) + salt) == expected
