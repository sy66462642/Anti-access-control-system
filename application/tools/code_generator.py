
import hashlib

def code_generator(id):
    str_id = bytes(id)
    m=hashlib.sha256(str_id)
    res_str=m.hexdigest()
    return res_str[:16]

