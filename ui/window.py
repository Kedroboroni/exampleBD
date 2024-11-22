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

        self.centralGrid = GridLayout() #Сетка для размещения областей программы
        self.centralWidget.setLayout(self.centralGrid)

        self.sidebarWidget = sidebarWidget() #виджет в котором расположены кнопки боковой панели (для кастомного оформления)
        self.workSpaceWidget = workSpaceWidget()
        self.errorWidget = errorWidget()

        self.centralGrid.addWidget(self.sidebarWidget, 0, 0,  1, 1)
        self.centralGrid.addWidget(self.workSpaceWidget, 0, 1, 1, 1)
        self.centralGrid.addWidget(self.errorWidget, 1, 0, 1, 2)

        self.sidebar = VBoxLayout()
        self.workSpace = VBoxLayout()
        self.error = VBoxLayout()

        self.sidebarWidget.setLayout(self.sidebar)
        self.workSpaceWidget.setLayout(self.workSpace)
        self.errorWidget.setLayout(self.error)

        btn11 = Button(text = "test")
        btn12 = Button(text = "test")
        btn13= Button(text = "test")
        btn14= Button(text = "test")
        self.sidebar.addWidget(btn11)
        self.sidebar.addWidget(btn12)
        self.sidebar.addWidget(btn13)
        self.sidebar.addWidget(btn14)

        btn2 = Button(text = "test")
        self.workSpace.addWidget(btn2)
        
        btn3 = Button(text = "test")
        self.error.addWidget(btn3)



        

        #self.sidebarWidget.set



    def contentSidebar(self):

        pass
        
    

        


        



    def contentTabWidgets(self): # тут в названии при определнии контента, пишим какой период на вкладке

        pass    


""" @Slot()
    def runVideoThreding(self):
        self.threadVideo =videoThread(nameWeights, self.LineEditPath.text())
        self.threadVideo.pixmapSignal.connect(lambda: startVideo(self.LableStream, modelName, self.LineEditPath.text()))
        self.threadVideo.start()"""