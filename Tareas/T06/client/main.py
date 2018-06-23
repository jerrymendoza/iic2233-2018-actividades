
import sys
from PyQt5 import uic
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QApplication, QMessageBox
import core
"""
Creamos nuestra ventana principal heredando desde la GUI creada con Designer.
La función loadUiType retorna una tupla en donde el primer elemento
corresponde al nombre de la ventana definido en QtDesigner, y el segundo
elemento a la clase base de la GUI.
"""

window_name, base_class = uic.loadUiType("main-client.ui")


class MainWindow(window_name, base_class):
    def __init__(self):
        super().__init__()
        self.core = core.Core()
        self.setupUi(self)

        #self.editButton.clicked.connect(self.setListos)
        self.downloadButton.clicked.connect(self.download)
        self.createButton.clicked.connect(self.test)
        
        self.core.lista_check.connect(self.setListos)
     


    def test(self):
        """
        Este método controla la acción ejecuta cada vez que presionamos el
        botón1.
        """

        boton = self.sender()
        #QMessageBox.warning(self, '', "boton "+boton.text())


    def setListos(self,lista):

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
        self.core.user(self.lineEditUser.text())

    def download(self):

        self.core.download(self.listView_2.currentIndex().data())



if __name__ == '__main__':
    app = QApplication([])
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())