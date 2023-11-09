import io
import sys
import random

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainW</class>
 <widget class="QMainWindow" name="MainW">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>YellowC</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="yellow">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>75</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>PushButton</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class Yellow(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.do_paint = False
        self.yellow.clicked.connect(self.paint)

    def do(self, qp):
        xl, yl, diam = random.choice(range(100, 650)), random.choice(
            range(100, 450)), random.choice(range(10, 130))
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(xl, yl, diam, diam)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.do(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Yellow()
    ex.show()
    sys.exit(app.exec_())
