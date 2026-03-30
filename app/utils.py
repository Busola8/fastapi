from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash(password: str):
    print("Hashing password:", repr(password), "Length:", len(password))
    return pwd_context.hash(password.strip())


def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

