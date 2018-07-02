import re
def bool_str(bool):
    if bool:
        return "Activado"
    else:
        return "Desactivado"

def list_to_str(list):
    _str=''
    for i in list:
        _str+=str(i)+','

    return _str[:-1]

def isvalid(mail):
    pattern = "([a-zA-Z0-9_.+-]+@[a-zA-Z]+\.{1}[a-zA-Z]+$)"
    if bool(re.match(pattern, mail)):
        return True
    else:
        return False