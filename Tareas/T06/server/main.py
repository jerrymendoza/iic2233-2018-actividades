import threading
import socket
import json
import os
import core
class Server:
    def __init__(self):

        self.methods = {'request': self.request}
        self.core = core.Core()



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

        print(" {:^8}| {:^15} | {:^10}".format("Cliente","Acción","Detalles"))

        self.sockets = []


    def accept_connections_thread(self):

        while True: 
            client_socket, client_address = self.socket_servidor.accept()
            
            self.sockets.append(client_socket)

            print(" {:^8}| {:15} | {}".format(
                self.sockets.index(client_socket)+1,"Conectarse","-"))
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

            order = decoded['status']
            if order == 'desconectar':
                print(" {:^8}| {:15} | {}".format(
                self.sockets.index(client_socket)+1,"Desconectarse","-"))
                self.sockets.remove(client_socket)
                break
            else:    
                self.handle_command(decoded, client_socket)

                

    def handle_command(self, received, client_socket):
        '''
        Este método toma lo recibido por el cliente correspondiente al socket pasado
        como argumento.
        :param received: diccionario de la forma: {"status": tipo, "data": información}
        :param client_socket: socket correspondiente al cliente que envió el mensaje
        :return:
        '''
        #print("Mensaje Recibido: ", received)
        order = received['status']
        if order != 'desconectar':
            foo = self.methods[order]
            foo(client_socket, received)

    @staticmethod
    def send(value, socket=None):
        '''
        Este método envía la información al cliente correspondiente al socket.
        :param msg: diccionario del tipo {"status": tipo del mensaje, "data": información}
        :param socket: socket del cliente al cual se le enviará el mensaje
        :return:
        '''

        if socket!=None:
            msg_json = json.dumps(value)
            msg_bytes = msg_json.encode()

            msg_length = len(msg_bytes).to_bytes(4, byteorder="big")

            socket.send(msg_length + msg_bytes)
        else:
            for sock in self.sockets:
                msg_json = json.dumps(value)
                msg_bytes = msg_json.encode()

                msg_length = len(msg_bytes).to_bytes(4, byteorder="big")

                sock.send(msg_length + msg_bytes)

    """
    Acciones a procesar

    """
    def request(self,client_socket,received):

        if received["data"]["header"]=="ready":
            midis_listos = self.core.listos()

            data = {"status": "result", 
                    "data":{'header':'ready', 'content':midis_listos} }
        
        elif received["data"]["header"]=="editing":
            midis_editando = list(*self.core.editando.keys())
            data = {"status": "result", 
                    "data":{'header':'editing', 'content':midis_editando} }

        elif received["data"]["header"] == "user":
            if not self.core.exist_user(received["data"]['content']):
                data = {"status": "result",
                        "data": {'header':'user', 
                            'content': received["data"]['content']}}

                print(" {:^8}| {:15} | {}".format(
                self.sockets.index(client_socket)+1,"Usuario",
                "A definido de usuario: "+received["data"]['content']) )
        elif received["data"]["header"] == "new":

            self.core.nuevo(received["data"]['content'],client_socket)

            print(" {:^8}| {:15} | {}".format(
                self.sockets.index(client_socket)+1,"Nuevo",
                "Crear midi: "+received["data"]['content']) )

            data = {"status": "result",
                    "data": {'header':'new', 
                            'content':received["data"]['content']}}


        elif received["data"]["header"] == "crear_nota":
            #agregar_nota(midi,usuario,nota)
            self.core.agregar_nota(received["data"]['content'],
                client_socket,received["data"]['content2'])

            data = {"status": "result",
                    "data": {'header':'crear_nota', 
                            'content':received["data"]['content'],
                            'content2':received["data"]['content2']}
                            }

        elif received["data"]["header"] == "eliminar_nota":
            #agregar_nota(midi,usuario,nota)
            self.core.eliminar_nota(received["data"]['content'],
                client_socket,received["data"]['content2'])

            data = {"status": "result",
                    "data": {'header':'nota', 
                            'content':received["data"]['content'],
                            'content2':received["data"]['content2']}
                            }

        elif received["data"]["header"] == "terminar":
    
            self.core.terminar(received["data"]['content'],
                client_socket)
            print(" {:^8}| {:15} | {}".format(
                self.sockets.index(client_socket)+1,"Edicion",
                "Edicion Terminada: "+received["data"]['content']) )

            data = {"status": "result",
                    "data": {'header':'terminar', 
                            'content':received["data"]['content']}
                            }

        elif received["data"]["header"] == "download":

            info = self.core.archivo(received["data"]['content'])

            print(" {:^8}| {:15} | {}".format(
                self.sockets.index(client_socket)+1,"Descargar",
                received["data"]['content']+" "+str(len(info)) ))

            data = {"status": "result",
                    "data":{'header':'download', 
                            'content':received["data"]['content'],
                            'size':len(info)
                            }}
            
            

        else: 
            data = {"status":None}

        self.send(data, client_socket)

        #Si es de tipo download, se recibe el midi a continuacion
        if received["data"]["header"] == "download":
            info = self.core.archivo(received["data"]['content'])
            contar=1
            for dat in cortar(info,1024):
                print(" {:^8}| {:15} | {}".format(
                self.sockets.index(client_socket)+1,"Enviando",
                received["data"]['content']+" Parte "+str(contar) ))
                client_socket.send(dat)
                contar+=1
            print(" {:^8}| {:15} | {}".format (
                self.sockets.index(client_socket)+1,"Completado",
                received["data"]['content'] ))

    def actualizar(self):
        midis_listos = self.core.listos()
        midis_edicion = self.core.editando.keys()
        data = {"status": "result", 
                    "data":{'header':'ready', 'content':midis_listos}}
        self.send(data, None)
        data = {"status": "result", 
                    "data":{'header':'editing', 'content':midis_edicion}}
        self.send(data, None)  

def cortar(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]


if __name__ == '__main__':
    server = Server()

    # Mantenemos al server corriendo
    while True:
        pass