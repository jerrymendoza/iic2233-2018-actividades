import re
import requests
import json
import random

def validar_correo(correo):
    """
    Retorna True si el formato del correo es valido y si el servidor existe,
    en otro caso retorna False
    :param correo: str
    :return: bool
    """
    pattern = "([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    if not bool(re.match(pattern, correo)):
        return False

    pattern2 = "@([a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
    try:
        dominio = re.search(pattern2, correo).group(1)
    except:
        return False
    url = "http://"+dominio
    r=requests.get(url)
    
    if r.status_code < 400:
        return True
    else: 
        return False


def obtener_mejores():
    """
    Retorna una muestra aleatoria de 10 memes provenientes de los 100 mejores
    :return: [dict]
    """
    URL = "https://api.imgflip.com/get_memes"
    los_memes = requests.get(URL).json().get('data').get('memes')
    #json_dict = json.loads(my_api)
    return random.sample(los_memes,10)


def generar_meme(template_id, username, password, text0, text1):
    """
    Genera un meme correspondiente al template_id con texto superior text0
    y texto inferior text1. Retorna la url al meme
    :param template_id: int
    :param username: str
    :param password: str
    :param text0: str
    :param text1: str
    :return: str
    """
    print(username)
    print(password)

    URL = "https://api.imgflip.com/caption_image"

    dic = {'template_id': template_id,
           'username':username,'password':password, 
           'text0': text0, 'text1': text1}

    r = requests.post(URL, data=dic).json().get('data').get('url')
    return r

print(generar_meme(54474703,'JERRYMENDOZA','12345','hola','chao'))