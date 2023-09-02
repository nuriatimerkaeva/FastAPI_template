from passlib.context import CryptContext


class PasswordManager:
    HASH_SCHEME = ["argon2"]
    hasher = CryptContext(schemes=HASH_SCHEME, deprecated="auto")

    def encode_password(self, password: str) -> str:
        return self.hasher.hash(password)

    def verify_password(self, password: str, encoded_password: str) -> bool:
        return self.hasher.verify(password, encoded_password)