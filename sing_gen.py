from hashlib import sha256
from config import SECRET_KEY

def sign_gen(data):
    str_gen = ":".join(data) + SECRET_KEY
    sign = sha256(str_gen.encode('utf-8')).hexdigest()
    return sign