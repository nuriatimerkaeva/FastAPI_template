from datetime import datetime, timedelta
import jwt
from fastapi import HTTPException

from src.core.settings import load_settings

class Auth:

    def _generate_token(self, username, scope, expiration_time):
        payload = {
            'exp': datetime.utcnow() + timedelta(**expiration_time),
            'iat': datetime.utcnow(),
            'scope': scope,
            'sub': username
        }
        return jwt.encode(payload, load_settings.SECRET_KEY, algorithm='HS256')

    def _verify_token(self, token, expected_scope):
        try:
            payload = jwt.decode(token, load_settings.SECRET_KEY, algorithm='HS256')
            if payload['scope'] == expected_scope:
                return payload['sub']
            raise HTTPException(status_code=401, detail='Token scope is invalid')
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail='Token expired')
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail='Invalid Token')

    def encode_token(self, username):
        return self._generate_token(username, 'access_token', {'days': 0, 'minutes': 10})

    def decode_token(self, token):
        return self._verify_token(token, 'access_token')

    def encode_refresh_token(self, username):
        return self._generate_token(username, 'refresh_token', {'days': 0, 'hours': 10})

    def refresh_token(self, refresh_token):
        return self._verify_token(refresh_token, 'refresh_token')