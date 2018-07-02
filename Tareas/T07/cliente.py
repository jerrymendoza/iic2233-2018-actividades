import requests
import lib

URL = 'http://127.0.0.1:5000/'
while True:
    mail = input("Mail: ")
    if lib.isvalid(mail):
        break
    else: 
        print("No valido, intenta nuevamente")

ciudades = [] #santiago 3873544
ciudades2 = {}
tiempo = {'actual':True,
          '5dias':True,
          'descripcion':True,
          'temperatura':True,
          'presion':True,
          'humedad':True,
          't_min':True,
          't_max':True,
          'velocidad':True,
          'nubosidad':True,
          }
nombre_tiempo = ['Día actual','Proximos 5 días', 'Descripción',
                'Temperatura','Presion','Humedad','Temperatura minima',
                'Temperatura maxima','Velocidad Viento','Nubosidad']

uv = {'actual':True,
      '8dias':True,
}
nombre_uv = ['Día actual','Proximos 5 días']

unidad = 'metric' #crear menu

while True:
    print("Ingresar Ciudad")
    print ("""
    1.Por coordenadas
    2.Por id
    3.Por nombre
    4.Continuar
    """)

    ans=input("¿Que te gustaria realizar? ")

    if ans=="1":
        lat = input("Ingresar Latitud: ")
        lon = input("Ingresar Longitud: ")
        print("Buscando...")
        consulta = requests.get(URL+"coord?lat="+lat+"&lon="+lon)
        consulta = consulta.json()
        if consulta["success"]== True:
            ciudades.append(str(consulta["data"]['id'])) 
            ciudades2[str(id)]=consulta["data"]['name']
            print("Hemos agregado {} a tu lista de envio".format(
                consulta["data"]['name'])) 
            print("\n")
        else:
            print("No encontrado, Intenta nuevamente")


    elif ans=="2":
        id = input("Ingresar ID: ")
        print("Buscando...")
        consulta = requests.get(URL+"id?id="+id)
        consulta = consulta.json()
        if consulta["success"]== True:
            ciudades.append(str(consulta["data"]['id'])) 
            ciudades2[str(id)]=consulta["data"]['name']
            print("Hemos agregado {} a tu lista de envio".format(
                consulta["data"]['name'])) 
            print("\n")
        else:
            print("No encontrado, Intenta nuevamente")

    elif ans=="3":
        pais = input("Ingresar pais: ")
        nombre = input("Ingresar ciudad: ")
        print("Buscando...")
        consulta = requests.get(URL+"name?country="+pais+'&name='+nombre)
        consulta = consulta.json()
        if consulta["success"]== True:
            ciudades.append(str(consulta["data"]['id'])) 
            ciudades2[str(id)]=consulta["data"]['name']
            print("Hemos agregado {} a tu lista de envio".format(
                consulta["data"]['name'])) 
            print("\n")

        else:
            print("No encontrado, Intenta nuevamente")
    elif ans=="4":
        if len(ciudades)>0:

            print("\n")
            break
        else: 
            print("No puedes continuar si no ingresas alguna ciudad")
    else:
        print("\n Opcion no valida, intenta nuevamente")

while True:
    print("Unidades: ")
    print ("""
    1.Fahrenheit
    2.Celsius
    3.Kelvin

    """)

    ans=input("¿Que unidad prefieres? ")
    if ans=="1":
        print("Elegiste Fahrenheit! \n")
        unidad = 'imperial'
        break
    elif ans=="2":
        print("Elegiste Celsius! \n")
        unidad = 'metric'
        break
    elif ans=="3":
        print("Elegiste Kelvin! \n")
        unidad = 'kelvin'
        break
while True:
    print ("""
    1.Ver configuración actual
    2.Cambiar configuración de reportes
    3.Mandar reporte del tiempo
    4.Cerrar sesión
    """)

    ans=input("¿Que te gustaria realizar? ")

    if ans=="1":
        print("\n {:^50}".format('Configuracion Actual')) 
        aux = list(tiempo.values())
        for i in range(len(tiempo)):
            print("{:<30}{:>20}".format(nombre_tiempo[i], lib.bool_str(aux[i])))


    elif ans=="2":
        print("\n Cambiar configuración de reportes") 

    elif ans=="3":

        print("\n Mandar reporte del tiempo")
        list3_aux = [str(int(elem)) for elem in list(tiempo.values())]
        values_tiempo = ''.join(list3_aux)

        values_uv = ''.join([str(int(elem)) for elem in list(uv.values())])

        ids = lib.list_to_str(ciudades)

        consulta_str = '{}request?tiempo={}&uv={}&sistema={}&mail={}&ids={}'.format(
                URL, values_tiempo, values_uv, unidad, mail, ids)



        consulta = requests.get(consulta_str)

        if consulta.json()['success']:
            print(" Correo enviado exitosamente!!")

    elif ans=="4":
        print("\n Adios!")
        break

    else:
        print("\n Opcion no valida, intenta nuevamente") 

