from cryptography.fernet import Fernet
from make_key import key_maker


def AES_encrypt(text, pas, salt="_i start work__________!____"):
    salt = salt.encode()
    text = text.encode()
    password = pas.encode()
    key = key_maker(pas, salt)
    f = Fernet(key).encrypt(message)
    return f