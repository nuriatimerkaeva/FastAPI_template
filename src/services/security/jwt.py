from typing import Dict, Union
from datetime import datetime, timedelta
import jwt
from fastapi import HTTPException

from src.core.settings import load_settings


class Auth:
    def generate_token(self, username, scope, expiration_time):
        payload = {
            'exp': datetime.utcnow() + timedelta(**expiration_time),
            'iat': datetime.utcnow(),
            'scope': scope,
            'sub': username
        }
        return jwt.encode(payload, load_settings.secret_key, algorithm='HS256')

    def verify_token(self, token, expected_scope):
        try:
            payload = jwt.decode(token, load_settings.secret_key, algorithm='HS256')
            if payload['scope'] == expected_scope:
                return payload['sub']
            raise HTTPException(status_code=401, detail='Token scope is invalid')
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail='Token expired')
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail='Invalid Token')

    def create_access_token(data: dict, expires_delta: timedelta | None = None) -> Dict[str, Union[str, datetime]]:
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=10)
        to_encode.update({"exp": expire, "sub": "access"})
        encoded_jwt = jwt.encode(to_encode, load_settings().SECRET_KEY, algorithm="HS256")
        return encoded_jwt
