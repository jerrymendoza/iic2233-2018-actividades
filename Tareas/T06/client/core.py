import threading
import socket
import json
from PyQt5.QtCore import pyqtSignal, QObject

class Core(QObject):
    """
    Encargado de manejar la info con el servidor
    """
    lista_check = pyqtSignal(list)
    def __init__(self):
        super().__init__()
        print("Inicializando cliente...")

        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.host = "localhost"

        self.port = 12345

        try:

            self.socket_cliente.connect((self.host, self.port))
            print("Cliente conectado exitosamente al servidor...")

            # hacemos True un boolean para que escuche
            self.connected = True

            thread = threading.Thread(target=self.listen_thread, daemon=True)
            thread.start()
            print("Escuchando al servidor...")
            

        except ConnectionRefusedError:
            # Si la conexión es rechazada, entonces se 'cierra' el socket
            print("Conexión terminada")
            self.socket_cliente.close()
            exit()

        finally:
            #obtener cosas inicial
            self.ready()

    def listen_thread(self):
        '''
        Este método es el usado en el thread y la idea es que reciba lo que
        envía el servidor. Implementa el protocolo de agregar los primeros
        4 bytes, que indican el largo del mensaje
        :return:
        '''

        # Si desean que un usuario pueda desconectarse
        while self.connected:
            # Primero recibimos los 4 bytes del largo
            response_bytes_length = self.socket_cliente.recv(4)
            # Los decodificamos
            response_length = int.from_bytes(response_bytes_length,
                                             byteorder="big")

            # Luego, creamos un bytearray vacío para juntar el mensaje
            response = bytearray()

            # Recibimos datos hasta que alcancemos la totalidad de los datos
            # indicados en los primeros 4 bytes recibidos.
            while len(response) < response_length:
                response += self.socket_cliente.recv(1024)

            # Una vez que tenemos todos los bytes, entonces ahí decodificamos
            response = response.decode()

            # Luego, debemos cargar lo anterior utilizando json
            decoded = json.loads(response)

            # Para evitar hacer muy largo este método, el manejo del mensaje se
            # realizará en otro método
            self.handlecommand(decoded)

    def handlecommand(self, decoded):
        '''
        Este método toma el mensaje decodificado de la forma:
        {"status": tipo del mensaje, "data": información}
        :param decoded: diccionario con la información
        :return:
        '''

        # Podemos imprimir para verificar que toodo anda bien
        print("Mensaje Recibido: {}".format(decoded))

        # Vemos si el tipo de mensaje es de resultado
        if decoded["status"] == "result":
            # Si lo es, entonces tomamos la información y emitimos una señal
            data = decoded["data"]
            if data["header"] == "ready":
                self.lista_check.emit(data['content'])

            #event = ResultadosEvent(data["eleccion_1"], data["eleccion_2"],
            #                        data["res"])
            #self.trigger_resultados.emit(event)

            #Recibir archivo midi si es necesario!
            elif data["header"] == "download":
                print("descargando el midi")
                print(data["size"])
                response = bytearray()
                while len(response) < data["size"]:
                    response += self.socket_cliente.recv(1024)
                in_file = open(data['content']+".mid", "wb")
                in_file.write(response)
                in_file.close()

        # Aquí irían otras opciones
        # elif decoded["status"] == "logout": # Ejemplo!
            # hacer algo


    def send(self, msg):
        '''
        Este método envía la información al servidor. Recibe un mensaje del tipo:
        {"status": tipo del mensaje, "data": información}
        :param msg: diccionario con la información
        :return:
        '''
        # Le hacemos json.dumps y luego lo transformamos a bytes
        msg_json = json.dumps(msg)
        msg_bytes = msg_json.encode()

        # Luego tomamos el largo de los bytes y creamos 4 bytes de esto
        msg_length = len(msg_bytes).to_bytes(4, byteorder="big")

        # Finalmente, los enviamos al servidor
        self.socket_cliente.send(msg_length + msg_bytes)



    """
    Acá se escriben las peticiones a enviar!
    """
    def ready(self):
        data = {"status": "request", "data": {'header':'ready','content':''}}
        self.send(data)

    def user(self, user):
        data = {"status": "request", "data": {'header':'user', 'content': user}}
        self.send(data)

    def new(self,name):
        data = {"status": "request", "data": {'header':'new', 'content': name}}
        self.send(data)

    def download(self,name):
        data = {"status": "request", "data": {'header':'download', 'content': name}}
        self.send(data)
