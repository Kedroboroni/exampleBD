import sys, os
sys.path.append(os.path.dirname(
                os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from PySide6.QtWidgets import QStackedWidget, QTableWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QWidget, QLineEdit, QSizePolicy
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPixmap, QImage
from widgets.sidebarWidget import sidebarWidget
from tabWidget import tabWidget
from labels.sidebarLabel import sidebarLabel


class workSpaceWidget(QStackedWidget):

    def __init__(self):

        super().__init__()
        self.placment()

        #1. В placment определить сначала приветсвенный экран!
        #2. Опеределить методы по вкладкам (1 метод - 1 вкладка и размещение там, + retunr widget)
    
    def placment(self):
         
        self.addWidget(self.welcome()) #0
        self.addWidget(self.tabels()) #1
        self.addWidget(self.analyse()) #2
        self.addWidget(self.DB()) #3
        self.addWidget(self.users()) #4
        self.addWidget(self.report())


    def welcome(self):
        #!!!!сейча сбуду использовать классическую табилцу,
        #!!!!Далее нужно будет ее переопредилть, явно укзаать откуда брать данные
        #!!!!Класс таблица будет в папке tabel
        widget = QWidget()
        layout = QHBoxLayout()
        widget.setLayout(layout)
        self.setLayout(layout)
        layout.setContentsMargins(0, 0, 0, 0)

        self.welcomeLabel = QLabel()
        image = QImage(r"C:\WorkSpace\Python\projectGSH\ui\widgets\workerSpaceWidget\welcome.jpg")
        self.welcomeLabel.setPixmap(QPixmap(image))
        self.welcomeLabel.setScaledContents(True)
        layout.addWidget(self.welcomeLabel)
        
        return widget


    def tabels(self):
         
        widget = QWidget()
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        widget.setLayout(layout)

        self.tabs = tabWidget(5)
        layout.addWidget(self.tabs)

        return widget
    

    def analyse(self):
         
        widget = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        widget.setLayout(layout)

        image = QImage(r"C:\WorkSpace\Python\projectGSH\ui\widgets\workerSpaceWidget\Label3.jpg")

        self.label = QLabel()
        self.label.setScaledContents(True)
        layout.addWidget(self.label)
        self.label.setPixmap(QPixmap(image))

        return widget
        
    
    def DB(self):
         
        widget = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        widget.setLayout(layout)

        image = QImage(r"C:\WorkSpace\Python\projectGSH\ui\widgets\workerSpaceWidget\Label2.jpg")

        self.label = QLabel()
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label.setScaledContents(True)
        layout.addWidget(self.label)
        self.label.setPixmap(QPixmap(image))

        return widget


    def users(self):
         
        widget = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        widget.setLayout(layout)
        layout.setAlignment(Qt.AlignCenter)

        #Создать условие для входа пользователя if asda= das 

        LOGIN = QLineEdit()
        LOGIN.setFixedSize(250,50)
        layout.addWidget(LOGIN)

        PASSWORD = QLineEdit()
        PASSWORD.setFixedSize(250,50)
        PASSWORD.setEchoMode(QLineEdit.Password)
        layout.addWidget(PASSWORD)

        btnSignUP = QPushButton("Войти")
        btnSignUP.setFixedSize(250,50)
        layout.addWidget(btnSignUP)

        return widget
    

    def report(self):

        widget = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        widget.setLayout(layout)

        image = QImage(r"C:\WorkSpace\Python\projectGSH\ui\widgets\workerSpaceWidget\Label4.jpg")

        self.label = QLabel()
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label.setScaledContents(True)
        layout.addWidget(self.label)
        self.label.setPixmap(QPixmap(image))

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

    #l2 = QHBoxLayout()
   #secondWidget.setLayout(l2)
    
    #btn2 = QPushButton("Кнопка")
    #l2.addWidget(btn2)

    window.resize(512, 300)
    window.show()
    sys.exit(app.exec())
        
        
        