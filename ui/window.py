""" 
Файл в котором, размещены кнопки,
указанны ссылки на собития и указаны
ссылки на стили 
"""

from widgets import *
from objects import *
from PySide6.QtWidgets import QMainWindow, QPushButton
#from events import openFile, startVideo, pauseVideo, resumeVideo


nameWeights = "best.pt"

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.mainWindow()
        
    def mainWindow(self):
        """Размещаем свои виджеты"""
        self.centralWidget = centralWidget() #Создали центарльный виджет в котором будут располагаться другие виджеты
        self.setCentralWidget(self.centralWidget) #Разместили центральныйтвиджет в главном окне

        self.centralGrid = GridLayout() #Сетка для размещения областей программы
        self.centralWidget.setLayout(self.centralGrid)

        self.sidebarWidget = sidebarWidget() #виджет в котором расположены кнопки боковой панели (для кастомного оформления)
        self.centralGrid.addWidget(self.sidebarWidget)

        self.sidebarLayout = VBoxLayout()
        self.sidebarWidget.setLayout(self.sidebarLayout)

        btn1 = QPushButton("test")
        btn2 = QPushButton("test")
        btn3 = QPushButton("test")

        self.sidebarLayout.addWidget(btn1)
        self.sidebarLayout.addWidget(btn2)
        self.sidebarLayout.addWidget(btn3)
    

        


        



    def contentTabWidgets(self): # тут в названии при определнии контента, пишим какой период на вкладке

        pass    


""" @Slot()
    def runVideoThreding(self):
        self.threadVideo =videoThread(nameWeights, self.LineEditPath.text())
        self.threadVideo.pixmapSignal.connect(lambda: startVideo(self.LableStream, modelName, self.LineEditPath.text()))
        self.threadVideo.start()"""