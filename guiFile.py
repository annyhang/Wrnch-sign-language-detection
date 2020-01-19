#Code reference from (Stack Overflow)
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Button(QPushButton):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
    def QDragEnterEvent(self, e):
        m = e.mimeData()
        if m.hasUrls():
            e.accept()
        else:
            e.ignore()

    def QDropEvent(self, e):
        m = e.mimeData()
        if m.hasUrls():
            self.parent().label.setPixmap(QPixmap(m.urls()[0].toLocalFile()))

class Image(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        button = Button("", self)
        button.resize(100, 100)
        button.setIcon(QIcon("tempA.jpg"))
        button.setIconSize(QSize(100, 100))
        button.move(0, 0)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('tempB.jpg'))
        self.label.move(150, 150)
        self.setWindowTitle('Simple drag & drop')
        self.setGeometry(300, 300, 300, 300)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Image()
    ex.show()
    app.exec_()
