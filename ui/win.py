import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QGridLayout,QPushButton, QWidget
from window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    centralWidget = QWidget()
    window.setCentralWidget(centralWidget)
    window.setGeometry(280,200, 800, 620)

    grid = QGridLayout()
    


    bt1 = QPushButton("One")
    bt2 = QPushButton("Two")
    bt3 = QPushButton("Three")
    bt4 = QPushButton("Four")
    bt5 = QPushButton("Five")

    bt1.setFixedSize(50, 50)

    grid.addWidget(bt1, 0, 0)
    grid.addWidget(bt2, 1, 0)
    grid.addWidget(bt3, 2, 0)
    grid.addWidget(bt4, 3, 0)
    grid.addWidget(bt5, 4, 0)


    bt11 = QPushButton("One")
    bt21 = QPushButton("Two")
    bt31 = QPushButton("Three")
    bt41 = QPushButton("Four")
    bt51 = QPushButton("Five")

    grid.addWidget(bt11, 0, 1)
    grid.addWidget(bt21, 1, 1)
    grid.addWidget(bt31, 2, 1)
    grid.addWidget(bt41, 3, 1)
    grid.addWidget(bt51, 4, 1)

    centralWidget.setLayout(grid)
    window.show()

    sys.exit(app.exec())
