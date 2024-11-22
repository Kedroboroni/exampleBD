import sys, os
sys.path.append(os.path.dirname(
                os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from PySide6.QtWidgets import QStackedWidget, QTableWidget, QLabel, QHBoxLayout, QPushButton, QWidget, QLineEdit
from PySide6.QtCore import QSize
from PySide6.QtGui import QPixmap, QImage
from widgets.sidebarWidget import sidebarWidget
from tabWidget import tabWidget

class workSpaceWidget(QStackedWidget):

    def __init__(self):

        super().__init__()
        self.placement()
        #1. В placment определить сначала приветсвенный экран!
        #2. Опеределить методы по вкладкам (1 метод - 1 вкладка и размещение там, + retunr widget)
        
    def placement(self):
        #!!!!сейча сбуду использовать классическую табилцу,
        #!!!!Далее нужно будет ее переопредилть, явно укзаать откуда брать данные
        #!!!!Класс таблица будет в папке tabel

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        self.tabel = QPushButton("Кнопка вместо табилцы")
        self.tabel.setFixedSize(150,150)
        layout.addWidget(self.tabel)

        self.label = QPushButton("Воображаемый лейбл") #Тут необюхождимо определить, что нам нужно, какие виджеты еще (кнопки, графики и т.д)
        layout.addWidget(self.label)

    def tabels(self):
         
        widget = QWidget()
        layout = QHBoxLayout()
        widget.setLayout(QHBoxLayout)

        self.tabs = tabWidget()
        layout.addWidget(self.tabs)

        return widget
    

    def users(self):
         
        widget = QWidget()
        layout = QHBoxLayout()
        widget.setLayout(QHBoxLayout)

        #Создать условие для входа пользователя if asda= das 

        LOGIN = QLineEdit()
        layout.addWidget(LOGIN)

        PASSWORD = QLineEdit()
        PASSWORD.setEchoMode(QLineEdit.Password)
        layout.addWidget(PASSWORD)

        btnSignUP = QPushButton("Войти")
        btnSignUP.setFixedSize(250,50)
        layout.addWidget(btnSignUP)

        return widget

    def analyse(self):
         
        widget = QWidget()
        layout = QHBoxLayout()
        widget.setLayout(QHBoxLayout)

        image = QImage(r"Label3.png")

        self.label = QLabel()
        layout.addWidget(self.label)
        self.label.setPixmap(image)

        return widget


        




if __name__ == '__main__':

    from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QHBoxLayout, QPushButton
    app = QApplication(sys.argv)
    with open(r"ui\SpyBot.qss", "r") as file:
            style = file.read()
            app.setStyleSheet(style)  
    window = QMainWindow()
    centralWidget = QWidget()
    window.setCentralWidget(centralWidget)
    l = QHBoxLayout()

    l.setContentsMargins(0, 0, 0, 0)  
    l.setSpacing(0)
    centralWidget.setLayout(l)

    widget = sidebarWidget()
    secondWidget = workSpaceWidget()
    
    l.addWidget(widget)
    l.addWidget(secondWidget)

    l2 = QHBoxLayout()
    secondWidget.setLayout(l2)
    
    btn2 = QPushButton("Кнопка")
    l2.addWidget(btn2)

    window.resize(512, 300)
    window.show()
    sys.exit(app.exec())
        
        
        