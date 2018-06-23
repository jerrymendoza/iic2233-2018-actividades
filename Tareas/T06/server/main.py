import threading
import socket
import json
import os

class Server:
    def __init__(self):

        self.methods = {'request': self.request}

        print("Inicializando servidor...")
        self.host = "0.0.0.0"
        self.port = 12345
        self.socket_servidor = socket.socket(
            socket.AF_INET,socket.SOCK_STREAM)
        self.socket_servidor.setsockopt(
            socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.socket_servidor.bind((self.host,self.port))
        print("Dirección y puerto enlazados..")

        self.socket_servidor.listen()
        print("Servidor escuchando en {}:{}...".format(self.host, self.port))

        thread = threading.Thread(
            target=self.accept_connections_thread, daemon=True)
        thread.start()

        print("Servidor aceptando conexiones...")

        self.sockets = []


    def accept_connections_thread(self):

        while True: 
            client_socket, client_address = self.socket_servidor.accept()
            print("Nuevo Cliente Conectado")
            self.sockets.append(client_socket)

            listening_client_thread = threading.Thread(
                    target=self.listen_client_thread,
                    args=(client_socket,),
                    daemon=True
                )

            listening_client_thread.start()


    def listen_client_thread(self, client_socket):

        while True:
            response_bytes_length = client_socket.recv(4)
            response_length = int.from_bytes(response_bytes_length,
                                             byteorder="big")

            response = bytearray()

            while len(response) < response_length:
                response += client_socket.recv(1024)

            response = response.decode()

            decoded = json.loads(response)
            self.handle_command(decoded, client_socket)

    def handle_command(self, received, client_socket):
        '''
        Este método toma lo recibido por el cliente correspondiente al socket pasado
        como argumento.
        :param received: diccionario de la forma: {"status": tipo, "data": información}
        :param client_socket: socket correspondiente al cliente que envió el mensaje
        :return:
        '''
        print("Mensaje Recibido: ", received)
        order = received['status']
        if order != 'desconectar':
            foo = self.methods[order]
            foo(client_socket, received)

    @staticmethod
    def send(value, socket):
        '''
        Este método envía la información al cliente correspondiente al socket.
        :param msg: diccionario del tipo {"status": tipo del mensaje, "data": información}
        :param socket: socket del cliente al cual se le enviará el mensaje
        :return:
        '''

        # Le hacemos json.dumps y luego lo transformamos a bytes
        msg_json = json.dumps(value)
        msg_bytes = msg_json.encode()

        # Luego tomamos el largo de los bytes y creamos 4 bytes de esto
        msg_length = len(msg_bytes).to_bytes(4, byteorder="big")

        # Finalmente, los enviamos al servidor
        socket.send(msg_length + msg_bytes)

    """
    Acciones a procesar
    """
    def request(self,client_socket,received):

        if received["data"]["header"]=="ready":
            midis_listos = os.listdir("midis")

            data = {"status": "result", 
            "data":{'header':'ready', 'content':midis_listos} }

        elif received["data"]["header"] == "user":

            data = {"status": "result",
                    "data": {'header':'user', 
                            'content': received["data"]['content']}}

        elif received["data"]["header"] == "new":
            data = {"status": "result",
                    "data": {'header':'new', 
                            'content':received["data"]['content']}}

        elif received["data"]["header"] == "download":
            in_file = open("midis/"+received["data"]['content']+".mid", "rb")
            info = in_file.read()
            data = {"status": "result",
                    "data":{'header':'download', 
                            'content':received["data"]['content'],
                            'size':len(info)
                            }}
            in_file.close()
        else: 
            data = {"status":None}

        self.send(data, client_socket)

        if received["data"]["header"] == "download":
            in_file = open("midis/"+received["data"]['content']+".mid", "rb")
            info = in_file.read()
            print("enviando archivo")
            client_socket.send(info)
            in_file.close()




if __name__ == '__main__':
    server = Server()

    # Mantenemos al server corriendo
    while True:
        pass