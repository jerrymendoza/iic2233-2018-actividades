import flask
import requests
import gmail
import json
import sys
from datos import KEY_OPENWEATHER
gmail.get_credentials()
app = flask.Flask(__name__)
url = 'http://api.openweathermap.org/data/2.5/weather?'
url2 = 'http://api.openweathermap.org/data/2.5/weather?'

with open('city.list.json','r',encoding='utf8') as f:
    data = json.load(f)



@app.route("/")
def index():
    #test
    weather = requests.get(url+'id=3873544&units=imperial&appid='+KEY_OPENWEATHER)

    return flask.jsonify(weather.json())

@app.route("/coord", methods=["GET"])
def coord_lat_lon():
    lat = flask.request.args.get('lat')
    lon = flask.request.args.get('lon')
    encontrado=False
    for place in data:
        if str(place['coord']['lat'])==lat and str(place['coord']['lon'])==lon:
            id=place['id']
            name=place['name']
            encontrado=True
            break

    if encontrado:
        response = {"success": True,
                    "data": { "id": id, "name": name}
                    }
    else: 
        response = {"success": False}

    return flask.jsonify(response)

@app.route("/id", methods=["GET"])
def by_id():
    id = flask.request.args.get('id')
    encontrado=False
    for place in data:
        if str(place['id'])==id:
            id=place['id']
            name=place['name']
            encontrado=True

    if encontrado:
        response = {"success": True,
                    "data": { "id": id, "name": name}
                    }
    else: 
        response = {"success": False}

    return flask.jsonify(response)

@app.route("/name", methods=["GET"])
def by_name():
    country = flask.request.args.get('country')
    name = flask.request.args.get('name')

    encontrado=False
    for place in data:
        if place['name']==name and place['country']==country:
            id=place['id']
            name=place['name']
            encontrado=True

    if encontrado:
        response = {"success": True,
                    "data": { "id": id, "name": name}
                    }
    else: 
        response = {"success": False}

    return flask.jsonify(response)


@app.route("/request", methods=["GET"])
def request():

    tiempo = flask.request.args.get('tiempo')
    uv = flask.request.args.get('uv')
    sistema = flask.request.args.get('sistema')
    mail = flask.request.args.get('mail')
    ciudades = flask.request.args.get('ids')
    
    print(ciudades, file=sys.stderr)
    if ',' in ciudades:
        ciudades = ciudades.split(',')
    else:
        ciudades = [ciudades]
    print(ciudades, file=sys.stderr)
    #generar mail
    contenido_email = 'Hola!, \n'
    if tiempo[0]=="1": #si esta activo el de hoy
        for ciudad in ciudades:
            url_aux=url+'id='+ciudad+'&appid='+KEY_OPENWEATHER
            url_aux+="&lang=es" #espanol
            if sistema!='kelvin':
                url_aux+='&units='+sistema
            weather = requests.get(url_aux)
            data=weather.json()

            contenido_email+='Actual en '
            contenido_email+=data['sys']['country']+" "+data['name']+":\n"
            if tiempo[2]=="1":
                contenido_email+= '   Descripción: \n'
                for descripcion in data['weather']:
                    contenido_email+= '            '+descripcion['description']+'\n'

            if tiempo[3]=="1":
                contenido_email+= '   Temperatura: '+str(data['main']['temp'])+'\n'
            if tiempo[4]=="1":
                contenido_email+= '   Presión: '+str(data['main']['pressure'])+'\n'
            if tiempo[5]=="1":
                contenido_email+= '   Humedad: '+str(data['main']['humidity'])+'\n'
            if tiempo[6]=="1":    
                contenido_email+= '   T° Mínima: '+str(data['main']['temp_min'])+'\n'
            if tiempo[7]=="1":
                contenido_email+= '   T° Máxima: '+str(data['main']['temp_max'])+'\n'
            if tiempo[8]=="1":
                contenido_email+= '   Velocidad Viento: '+str(data['wind']['speed'])+'\n'
            if tiempo[9]=="1":
                contenido_email+= '   Nubosidad: '+str(data['clouds']['all'])+'\n'
            contenido_email+='\n'

    #if uv[1]=="1":
    #    for ciudad in ciudades:
    #        url_aux=url+'id='+ciudad+'&appid='+KEY_OPENWEATHER
    #        url_aux+="&lang=es" #espanol
    #        if sistema!='kelvin':
    #            url_aux+='&units='+sistema
    #        uv = requests.get(url_aux)










    #random quotes :D 
    quotes_random = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    quotes_random = quotes_random.json()
    url_yoda='http://api.funtranslations.com/translate/yoda.json?text='
    url_yoda+=quotes_random["quote"]
    yoda = requests.get(url_yoda)
    yoda = yoda.json()
    contenido_email+='\n \n'
    if "error" not in yoda.keys():
        
        contenido_email+=yoda['contents']['translated']
        contenido_email+='\n'
        contenido_email+=quotes_random["author"] +" ft. Yoda"

        contenido_email+='\n \n Original:'
        contenido_email+=yoda['contents']['text']

    else: 
        contenido_email+="Yoda esta duermiendo... vuelve mas tarde"

    gmail.main( 'me', mail, 'MaiWeather', contenido_email)
    response = {"success": True}


    return flask.jsonify(response)


if __name__ == "__main__":
   app.run(debug=True)
