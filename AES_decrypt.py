from cryptography.fernet import Fernet
from make_key import key_maker


def AES_decrypt(encrypted, pas, salt):
    salt = salt.encode()
    encrypted = encrypted.encode()
    password = pas.encode()
    key_maker(password, salt)
    f = Fernet(key).decrypt(encrypted)
    return f