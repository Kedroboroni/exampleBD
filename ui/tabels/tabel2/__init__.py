from PySide6.QtWidgets import QTableWidget, QSizePolicy, QTableWidgetItem
import numpy as np


class tabelPage2(QTableWidget):

    def __init__(self):

        super().__init__()
        self.setings()
        self.filling()

    def setings(self):

        self.setRowCount(20)
        self.setColumnCount(20)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def filling(self):

        data = np.random.randint(1, 100, size=(20, 10)) #Тут укажем БД
        """Тут мы укажем логику заполнения массива с БД"""
        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                self.setItem(i, j, QTableWidgetItem(str(data[i, j])))

if __name__ == "__main__":

    import sys

    from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QPushButton
    app = QApplication(sys.argv)

    with open(r"ui\SpyBot.qss", "r") as file:
            style = file.read()
            app.setStyleSheet(style)

    window = QMainWindow()
    widget = QWidget()
    window.setCentralWidget(widget)

    layout = QHBoxLayout()
    widget.setLayout(layout)

    table = tabelPage1()
    layout.addWidget(table)
    
    btn = QPushButton("Иммитация леблай")
    layout.addWidget(btn)

    window.show()
    sys.exit(app.exec())
    