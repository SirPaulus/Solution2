import io
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
import random
from PyQt5 import uic


class Test(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.draw = False
        self.createCircle.clicked.connect(self.circle)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.run(qp)

    def run(self, qp):
        if self.draw:
            x = random.randint(10, 150)
            y = random.randint(10, 150)
            w = random.randint(10, 100)
            h = random.randint(10, 100)
            qp.setPen(QColor(255, 255, 0))
            qp.drawEllipse(x, y, w, h)
            self.draw = False
            qp.end()

    def circle(self):
        self.draw = True
        self.update()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    w = Test()
    w.show()
    sys.exit(app.exec_())
