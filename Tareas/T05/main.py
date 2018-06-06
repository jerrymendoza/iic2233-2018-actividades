import sys
from collections import deque
from PyQt5.QtCore import (
    Qt,
    QBasicTimer,
    QUrl,
    QTimer
)
from PyQt5.QtGui import (
    QBrush,
    QPixmap,
    QColor
)
from PyQt5.QtWidgets import (
    QApplication,
    QGraphicsItem,
    QGraphicsPixmapItem,
    QGraphicsRectItem,
    QGraphicsScene,
    QGraphicsView
)

from PyQt5.QtMultimedia import (
    QMediaPlayer,
    QMediaContent
)


SCREEN_WIDTH            = 800
SCREEN_HEIGHT           = 600
PLAYER_SPEED            = 20   # pix/frame
FRAME_TIME_MS           = 120  # ms/frame
ASSETS = 'assets/'
MUSIC = 'assets/sound/'


class Player(QGraphicsPixmapItem):
    def __init__(self, parent = None):
        QGraphicsPixmapItem.__init__(self,parent)
        self.setPixmap(QPixmap(ASSETS+"down1.png"))
        self._down=deque(['down1.png','down2.png','down3.png'])
        self._up=deque(['up1.png','up2.png','up3.png'])
        self._right=deque(['right1.png','right2.png','right3.png'])
        self._left=deque(['left1.png','left2.png','left3.png'])

    def game_update(self, keys_pressed):
        dx = 0
        dy = 0
        if Qt.Key_Left in keys_pressed:
            self.setPixmap(QPixmap(ASSETS+self._left[0]))    
            self._left.rotate(1)
            if self.x()>0:
                dx -= PLAYER_SPEED
        if Qt.Key_Right in keys_pressed:
            self.setPixmap(QPixmap(ASSETS+self._right[0]))    
            self._right.rotate(1)
            if self.x()<SCREEN_WIDTH-48:  
                dx += PLAYER_SPEED

        if Qt.Key_Up in keys_pressed:
            self.setPixmap(QPixmap(ASSETS+self._up[0]))    
            self._up.rotate(1)
            if self.y()>0:
                dy -= PLAYER_SPEED

        if Qt.Key_Down in keys_pressed:
            self.setPixmap(QPixmap(ASSETS+self._down[0]))
            self._down.rotate(1)
            if self.y()<SCREEN_HEIGHT-48:
                dy += PLAYER_SPEED

        if Qt.Key_Space in keys_pressed:
            self.bomba = Bomba()
            self.bomba.setPos(self.x(),self.y())
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



class Scene(QGraphicsScene):
    def __init__(self, parent = None):
        QGraphicsScene.__init__(self, parent)

        self.keys_pressed = set()

        self.timer = QBasicTimer()
        self.timer.start(FRAME_TIME_MS, self)

        bg = QGraphicsRectItem()
        bg.setRect(0,0,SCREEN_WIDTH,SCREEN_HEIGHT)
        bg.setBrush(QBrush(QColor(31,139,0)))
        self.addItem(bg)

        self.player = Player()
        self.player.setPos((SCREEN_WIDTH-self.player.pixmap().width())/2,
                           (SCREEN_HEIGHT-self.player.pixmap().height())/2)

        

        self.musicabg = QMediaPlayer()
        self.musicabg.setMedia(QMediaContent(QUrl(MUSIC+'03_StageTheme.mp3')))
        self.musicabg.play()
        self.addItem(self.player)
        
        self.view = QGraphicsView(self)
        self.view.show()


    def keyPressEvent(self, event):
        self.keys_pressed.add(event.key())

        if Qt.Key_Control in self.keys_pressed and Qt.Key_P in self.keys_pressed:
            if not self.timer.isActive():
                self.timer.start(FRAME_TIME_MS,self)
                self.musicabg.play()

            else:
                self.timer.stop()
                self.musicabg.pause()



    def keyReleaseEvent(self, event):
        self.keys_pressed.remove(event.key())


    def timerEvent(self, event):
        self.game_update()
        self.update()

    def game_update(self):
        self.player.game_update(self.keys_pressed)

        for item in self.items():
            if type(item).__name__ == 'Bomba':
                item.game_update()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    scene = Scene()
    sys.exit(app.exec_())