from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor
import sys
from random import choice, randint

from PyQt5 import QtCore, QtGui, QtWidgets



class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)
        self.flag = False
        self.colors = ['Red', 'Orange', 'Yellow', 'Green', 'Cyan',
                       'Blue', 'Magenta', 'Purple', 'Brown', 'Black']
        self.pushButton.clicked.connect(self.run)

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.paint()
            self.qp.end()

    def run(self):
        self.flag = True
        self.repaint()

    def paint(self):
        x = randint(70, 300)
        y = randint(70, 300)
        z = randint(70, 300)
        self.qp.setBrush(QColor('Yellow'))
        self.qp.drawEllipse(720, 50, x, x)
        self.qp.drawEllipse(410, 250, y, y)
        self.qp.drawEllipse(100, 100, z, z)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())