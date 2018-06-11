import back
import sys
import time
from collections import deque
from PyQt5.QtCore import (
    Qt,
    QBasicTimer,
    QUrl,
    QTimer,
    pyqtSignal,
    QObject

)
from PyQt5.QtGui import (
    QBrush,
    QPixmap,
    QColor,
    QFont,
    QFontDatabase
)
from PyQt5.QtWidgets import (
    QWidget,
    QApplication,
    QGraphicsItem,
    QGraphicsPixmapItem,
    QGraphicsRectItem,
    QGraphicsScene,
    QGraphicsView,
    QGraphicsTextItem,
)

from PyQt5.QtMultimedia import (
    QMediaPlayer,
    QMediaPlaylist,
    QMediaContent
)

PUNTAJE_TIEMPO = 1
PATH = "mapa.txt"
SCREEN_WIDTH            = 1000
SCREEN_HEIGHT           = 800
PLAYER_SPEED            = 12  # pix/frame
FRAME_TIME_MS           = 120  # ms/frame
ASSETS = 'assets/'
MUSIC = 'assets/sound/'
N = 48 #pixeles,no modificar

MUSICA = False
class Player(QGraphicsPixmapItem):
    def __init__(self, parent = None):
        QGraphicsPixmapItem.__init__(self,parent)
        self.setPixmap(QPixmap(ASSETS+"down1.png"))
        self._down=deque(['down1.png','down2.png','down3.png'])
        self._up=deque(['up1.png','up2.png','up3.png'])
        self._right=deque(['right1.png','right2.png','right3.png'])
        self._left=deque(['left1.png','left2.png','left3.png'])

    def game_update(self, keys_pressed,mapa):
        dx = 0
        dy = 0
        if Qt.Key_Left in keys_pressed:
            self.setPixmap(QPixmap(ASSETS+self._left[0]))    
            self._left.rotate(1)
            #if self.x()>0:
            #    dx -= PLAYER_SPEED
            destino = (self.x()-PLAYER_SPEED,self.y())

            if mapa.mov_valido(destino):
                dx -= PLAYER_SPEED
            else: 
                print(self.x(),self.y())
                print(self.x()-PLAYER_SPEED)


        if Qt.Key_Right in keys_pressed:
            self.setPixmap(QPixmap(ASSETS+self._right[0]))    
            self._right.rotate(1)

            #if self.x()<SCREEN_WIDTH-48:
            destino = (self.x()+PLAYER_SPEED,self.y())
            if mapa.mov_valido(destino):  
                dx += PLAYER_SPEED
            else: 
                print(self.x(),self.y())
                print(self.x()+PLAYER_SPEED)

        if Qt.Key_Up in keys_pressed:
            self.setPixmap(QPixmap(ASSETS+self._up[0]))    
            self._up.rotate(1)
            #if self.y()>0:
            destino = (self.x(),self.y()-PLAYER_SPEED)
            if mapa.mov_valido(destino) : 
                dy -= PLAYER_SPEED
            else: 
                print(self.x(),self.y())
                print(self.y()-PLAYER_SPEED)

        if Qt.Key_Down in keys_pressed:
            self.setPixmap(QPixmap(ASSETS+self._down[0]))
            self._down.rotate(1)
            #if self.y()<SCREEN_HEIGHT-48:
            destino = (self.x(),self.y()+PLAYER_SPEED)
            if mapa.mov_valido(destino):  
                dy += PLAYER_SPEED
            else: 
                print(self.x(),self.y())
                print(self.y()+PLAYER_SPEED)

        if Qt.Key_Space in keys_pressed:
            self.bomba = Bomba()
            self.bomba.setPos(self.x(),self.y())
            mapa.bombas.append((self.x()//N,self.y()//N))
            self.scene().addItem(self.bomba)
        
       

        self.setPos(self.x()+dx, self.y()+dy)

class Bomba(QGraphicsPixmapItem):
    def __init__(self, parent = None):
        QGraphicsPixmapItem.__init__(self,parent)
        self.setPixmap(QPixmap(ASSETS+"bomba1.png"))
        self._img=deque(['bomba1.png','bomba2.png','bomba3.png'])
        
    def game_update(self):
        self.setPixmap(QPixmap(ASSETS+self._img[0]))
        self._img.rotate(1)




class Muralla(QGraphicsPixmapItem):
    def __init__(self, parent = None):
        QGraphicsPixmapItem.__init__(self,parent)
        self.setPixmap(QPixmap(ASSETS+"indestructible.png"))
        
    def game_update(self):
        pass

class Destructible(QGraphicsPixmapItem):
    def __init__(self, parent = None):
        QGraphicsPixmapItem.__init__(self,parent)
        self.setPixmap(QPixmap(ASSETS+"destructible1.png"))
        
    def game_update(self):
        pass




class Scene(QGraphicsScene):
    def __init__(self, parent = None):
        QGraphicsScene.__init__(self, parent)
        self.inicio = 0
        self.keys_pressed = set()

        self.timer = QBasicTimer()
        self.timer.start(FRAME_TIME_MS, self)
        self.time = QTimer()
        self.time.start(1000)

        


        self.time.timeout.connect(self.contar)

        bg = QGraphicsRectItem()
        bg.setRect(0,0,SCREEN_WIDTH,SCREEN_HEIGHT)
        bg.setBrush(QBrush(QColor(31,139,0)))
        self.addItem(bg)

        self.player = Player()
        #self.player.setPos((SCREEN_WIDTH-self.player.pixmap().width())/2,
        #                   (SCREEN_HEIGHT-self.player.pixmap().height())/2)
        self.player.setPos(800,48)
        #musica que se repite

        self.playlist = QMediaPlaylist()
        self.playlist.addMedia(QMediaContent(QUrl(MUSIC+'03_StageTheme.mp3')))
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)

        self.musicabg = QMediaPlayer()
        self.musicabg.setPlaylist(self.playlist)
        self.musicabg.play()
        self.musicabg.stop()

        #self.musicabg = QMediaPlayer()
        #self.musicabg.setMedia(QMediaContent(QUrl(MUSIC+'03_StageTheme.mp3')))
        #self.musicabg.play()
        self.addItem(self.player)
        
        self.mapa = back.Mapa(PATH)
        self.dibujar(self.mapa)


        self.tiempo = QGraphicsTextItem("{}:{}:{}".format(0,0,self.inicio))
        textofont= QFont("emulogic",12)
        self.tiempo.setFont(textofont)
        self.tiempo.setDefaultTextColor(Qt.white)

        self.tiempo.setPos(750,520)
        self.addItem(self.tiempo)

        self.view = QGraphicsView(self)
        #self.view.show()

    def contar(self):
        self.inicio+=1
        self.removeItem(self.tiempo)
        self.tiempo = QGraphicsTextItem("{}:{}:{}".format(0,0,self.inicio))
        textofont= QFont("emulogic",12)
        self.tiempo.setFont(textofont)
        self.tiempo.setDefaultTextColor(Qt.white)
        self.tiempo.setPos(750,520)
        self.addItem(self.tiempo)


    def dibujar(self,mapa):
        for indestruc in self.mapa.indestructibles:
            self.muralla = Muralla()
            self.muralla.setPos(indestruc[0]*N,indestruc[1]*N)
            self.addItem(self.muralla)

        for destruc in self.mapa.destructibles:
            self.destructible = Destructible()
            self.destructible.setPos(destruc[0]*N,destruc[1]*N)
            self.addItem(self.destructible)


    def keyPressEvent(self, event):
        self.keys_pressed.add(event.key())

        if (Qt.Key_Control in self.keys_pressed
            and Qt.Key_P in self.keys_pressed):
            if not self.timer.isActive():
                self.timer.start(FRAME_TIME_MS,self)
                self.musicabg.play()

            else:
                self.timer.stop()
                self.musicabg.pause()

        if (Qt.Key_Control in self.keys_pressed 
            and Qt.Key_E in self.keys_pressed):
            app.exit()



    def keyReleaseEvent(self, event):
        self.keys_pressed.remove(event.key())


    def timerEvent(self, event):
        self.game_update()
        self.update()

    def game_update(self):
        self.player.game_update(self.keys_pressed,self.mapa)

        for item in self.items():
            if type(item).__name__ == 'Bomba':
                item.game_update()

class Game(QGraphicsView):
    def __init__(self,parent = None):
        QGraphicsView.__init__(self, parent)

        self.setFixedSize(SCREEN_WIDTH,SCREEN_HEIGHT )
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.setBackgroundBrush(QBrush(Qt.black, Qt.SolidPattern));

        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0,0,SCREEN_WIDTH,SCREEN_HEIGHT)

        QFontDatabase.addApplicationFont(ASSETS+'emulogic.ttf')
        

        

        #musica
        self.musicho = QMediaPlayer()
        self.musicho.setMedia(QMediaContent(QUrl(MUSIC+'01_TitleScreen.mp3')))
        self.musicho.play()

        #logo
        logo = QGraphicsPixmapItem()
        logo.setPixmap(QPixmap(ASSETS+"codewithfire2.jpg"))
        logo.setPos(SCREEN_WIDTH/2-logo.pixmap().width()/2,40)
        self.scene.addItem(logo)

        #menu
        boton = Boton("Jugar")
        boton.setPos(SCREEN_WIDTH/2-boton.rect().width()/2,380)
        boton.s.escribe_signal.connect(self.start_stage)
        self.scene.addItem(boton)


        boton2 = Boton("Top 10")
        boton2.setPos(SCREEN_WIDTH/2-boton2.rect().width()/2,420)
        boton2.s.escribe_signal.connect(self.top10)
        self.scene.addItem(boton2)

        boton3 = Boton("Salir")
        boton3.setPos(SCREEN_WIDTH/2-boton3.rect().width()/2,460)
        boton3.s.escribe_signal.connect(self.close)
        self.scene.addItem(boton3)


        texto_pie = QGraphicsTextItem("Jerry Mendoza - IIC2233")
        textofont= QFont("emulogic",12)
        texto_pie.setFont(textofont)
        texto_pie.setDefaultTextColor(Qt.white)
        xt=self.width()/2-texto_pie.boundingRect().width()/2

        texto_pie.setPos(xt,520)
        self.scene.addItem(texto_pie)


        self.setScene(self.scene)

    def displayMenu(self):
        print("blabla")
        pass 
        
    def start_stage(self):
        self.scene.clear()
        text = "STAGE 1" #agregar numero
        stage_texto = QGraphicsTextItem(text)
        stage_texto.setFont(QFont("emulogic",12))
        stage_texto.setDefaultTextColor(Qt.white)
        xt=self.width()/2-stage_texto.boundingRect().width()/2
        yt=self.height()/2-stage_texto.boundingRect().height()/2
        stage_texto.setPos(xt,yt)
        self.scene.addItem(stage_texto)

        self.musicho.stop()
        self.musicstage = QMediaPlayer()
        self.musicstage.setMedia(QMediaContent(QUrl(MUSIC+'02_StageStart.mp3')))
        self.musicstage.play()

        self.timer2 = QTimer()
        self.timer2.timeout.connect(self.start_game)
        self.timer2.setSingleShot(True) 
        self.timer2.start(3500)
        

    def top10(self,lista=[]):

        lista=[("Jerry",300),("Jerry",38700),("Jerry",38700),("Jerry",38700),
        ("Jerry",38700),("Jerry",38700),("Jerry",38700),("Jerry",38700),
        ("Jerry",38700),("Jerry",38700)]

        self.scene.clear()
        titulo = "TOP 10"
        top10_titulo = QGraphicsTextItem(titulo)
        top10_titulo.setFont(QFont("emulogic",12))
        top10_titulo.setDefaultTextColor(Qt.white)
        xt=self.width()/2-top10_titulo.boundingRect().width()/2
        #yt=self.height()/2-stage_texto.boundingRect().height()/2
        yt=50
        top10_titulo.setPos(xt,yt)
        self.scene.addItem(top10_titulo)
        yt+=10
        
        for item in lista:
            yt+=44
            nombre = QGraphicsTextItem(item[0])
            nombre.setFont(QFont("emulogic",12))
            nombre.setDefaultTextColor(Qt.white)
            score = QGraphicsTextItem(str(item[1]))
            score.setFont(QFont("emulogic",12))
            score.setDefaultTextColor(Qt.white)

            nombre.setPos(150,yt)
            score.setPos(550,yt)

            self.scene.addItem(nombre)
            self.scene.addItem(score)

    def start_game(self):
        self.scene.clear()
        self.setScene(Scene())
       

    def close(self):
        app.exit()



class Boton(QGraphicsRectItem):
    def __init__(self,nombre,parent = None):
        QGraphicsRectItem.__init__(self, parent)
    
        self.s = MiSignal()

        self.setRect(0,0,200,40)
        self.setBrush(QBrush(Qt.black, Qt.SolidPattern))

        

        texto = QGraphicsTextItem(nombre,self)
        texto.setDefaultTextColor(Qt.white)
        texto.setFont(QFont('emulogic',15))
        x = self.rect().width()/2 - texto.boundingRect().width()/2
        y = self.rect().height()/2 - texto.boundingRect().height()/2
        texto.setPos(x,y)
        




        self.setAcceptHoverEvents(True)

    def mousePressEvent(self, event):
        self.s.escribe_signal.emit()

        
    
class MiSignal(QObject):
    """
    Esta clase contiene las señales que permiten la comunicación entre
    elementos de la GUI.
    """
    escribe_signal = pyqtSignal()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    #scene = Scene()
    game = Game()
    game.show()
    sys.exit(app.exec_())