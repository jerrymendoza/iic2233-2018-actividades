import sys
from PyQt5 import uic
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QApplication, QMessageBox
import core
import lib
"""
Creamos nuestra ventana principal heredando desde la GUI creada con Designer.
La función loadUiType retorna una tupla en donde el primer elemento
corresponde al nombre de la ventana definido en QtDesigner, y el segundo
elemento a la clase base de la GUI.
"""
form = None

window_name, base_class = uic.loadUiType("main-client.ui")
new_midi,base_class2 = uic.loadUiType("edit-client2.ui")

class MainWindow(window_name, base_class):
    def __init__(self):
        super().__init__()
        self.core = core.Core()
        self.setupUi(self)

        #self.editButton.clicked.connect(self.setListos)
        self.downloadButton.clicked.connect(self.download)
        self.createButton.clicked.connect(self.new)
        
        self.core.lista_check.connect(self.setListos)
     


    def test(self):
        """
        test
        """

        boton = self.sender()
        #QMessageBox.warning(self, '', "boton "+boton.text())


    def setListos(self,lista=[]):
        if not lista:
            self.core.get_ready()
            pass
        else:
            list = self.listView_2
            model = QStandardItemModel(list)

            for nombre in lista:
                # Create an item with a caption
                item = QStandardItem(nombre[:-4])
             
                # Add a checkbox to it
                item.setEditable(False)
             
                # Add the item to the model
                model.appendRow(item)
            list.setModel(model)

    def user(self):
        self.core.get_user(self.lineEditUser.text())

    def download(self):
        if self.listView_2.currentIndex().data():
            self.core.get_download(self.listView_2.currentIndex().data())

    def new(self):

        if self.lineEditNew.text():
            nuevo_midi= NewMidi(self,self.lineEditNew.text())
            nuevo_midi.show()

            #self.user()

            self.core.get_new(self.lineEditNew.text())


    def closeEvent(self, event):
        self.core.exit()
        QMessageBox.warning(self, '', "Desconectando")
        

        event.accept()
        exit()



class NewMidi(new_midi,base_class2):
    def __init__(self, parent, nombre):
        super(NewMidi,self).__init__(parent)
        self.setupUi(self)
        self.buttonAgregar.clicked.connect(self.agregar_nota)
        self.name = nombre
      
        self.model = QStandardItemModel(self.listViewNotas)
        self.listViewNotas.setModel(self.model)
        self.listViewNotas.clicked.connect(self.quitar_nota)


    def agregar_nota(self):
        if (self.nota.text() and self.escala.text() and
            self.intensidad.text() and self.duracion.text()):
            nota = lib.nota_octava(int(self.nota.text()),int(self.escala.text()))
            intensidad = int(self.intensidad.text())
            duracion = int(self.duracion.text())

            print("[{},{},{}]".format(nota,intensidad,duracion))
            form.core.nueva_nota(self.name,[nota,intensidad,duracion])

            item = QStandardItem("[{},{},{}]".format(nota,intensidad,duracion))

            item.setEditable(False)
            self.model.appendRow(item)


    def quitar_nota(self):
        index = self.sender().currentIndex().row()
        form.core.eliminar_nota(self.name,index)
        self.model.takeRow(index)
        

    def closeEvent(self, event):
        form.core.terminar(self.name)
        





if __name__ == '__main__':
    app = QApplication([])
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())