from PySide6.QtWidgets import QTabWidget, QWidget


class tabWidget(QTabWidget):

    def __init__(self, count):
        # !!! Тут вместо count будем указывтаь список с виджетами (в них размещены таблицы график, кнопки)
        super().__init__()

        for widget in range(count):
            self.addTab(QWidget(), f"{widget+1}")

    
if __name__ == '__main__':

    from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QHBoxLayout, QPushButton
    import sys
    app = QApplication(sys.argv)

    with open(r"ui\SpyBot.qss", "r") as file:
            style = file.read()
            app.setStyleSheet(style)  

    window = QMainWindow()
    centralWidget = QWidget()
    window.setCentralWidget(centralWidget)
    l = QHBoxLayout()

    #l.setContentsMargins(0, 0, 0, 0)  
    #l.setSpacing(0)
    centralWidget.setLayout(l)

    widget = tabWidget(5)
    #secondWidget = workSpaceWidget()
    
    l.addWidget(widget)
    #l.addWidget(secondWidget)

    #l2 = QHBoxLayout()
    #secondWidget.setLayout(l2)
    
    #btn2 = QPushButton("Кнопка")
    #l2.addWidget(btn2)

    window.resize(512, 300)
    window.show()
    sys.exit(app.exec())

    