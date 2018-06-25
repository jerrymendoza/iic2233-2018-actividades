import os
from PyQt5.QtCore import pyqtSignal, QObject
import lib

path_midis="midis"
class Core(QObject):
    def __init__(self):
        super().__init__()
        self.users = []
        self.editando = {}
                        #{nombre midi : {create_by: socket o user , notas: []},
                        # otros:[usuarios]}

    def listos(self):
        return os.listdir("midis")

    def nuevo(self,midi,usuario):
        """
        midi -> nombre del midi
        usuario-> creador del midi
        """
        self.editando[midi]={'create_by': usuario}
        self.editando[midi]['notas']= []

    def agregar_nota(self,midi,usuario,nota):
        if self.editando[midi]['create_by'] == usuario:
            self.editando[midi]['notas'].append(nota)

    def eliminar_nota(self,midi,usuario,index):
        if self.editando[midi]['create_by'] == usuario:
            del self.editando[midi]['notas'][index]


    def terminar(self,midi,usuario):
        if self.editando[midi]['create_by'] == usuario:
            lib.escribir_midi("midis/"+midi+'.mid',self.editando[midi]['notas'])
        


    def exist_user(self,nombre):
        return nombre in self.users

    #lee el archivo en bytes
    def archivo(self,nombre):
        with open("midis/"+nombre+".mid", "rb") as file:
            info = file.read()
        return info

if __name__ == '__main__':
    print(os.listdir("midis"))