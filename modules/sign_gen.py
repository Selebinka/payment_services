from hashlib import sha256
from config import SECRET_KEY

def sign_gen(data):
    list_keys = list(data.keys())
    list_keys.sort()
    sorted_value = []
    for i in list_keys:
        sorted_value.append(data[i])
    str_gen = ":".join(sorted_value) + SECRET_KEY
    sign = sha256(str_gen.encode('utf-8')).hexdigest()
    return sign