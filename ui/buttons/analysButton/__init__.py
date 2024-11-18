from PySide6.QtWidgets import QPushButton, QApplication, QWidget, QVBoxLayout
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import QSize
import sys



class analysButton(QPushButton):

    def __init__(self):

        super().__init__()

        self.setFixedSize(50,50)

        icon_path = r"ui\buttons\analysButton\analys.svg"
        icon = QIcon(QPixmap(icon_path))
        self.setIcon(icon)

        self.setIconSize(QSize(41,41))
        


if __name__ == "__main__":

    app = QApplication(sys.argv)
    with open(r"ui\SpyBot.qss", "r") as file:
            style = file.read()
            app.setStyleSheet(style)  
    window = QWidget()
    layout = QVBoxLayout()
    btn1 = analysButton()
    window.setLayout(layout)
    layout.addWidget(btn1)
    window.resize(300, 200)
    window.show()
    sys.exit(app.exec())
