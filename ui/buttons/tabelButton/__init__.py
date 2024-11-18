from PySide6.QtWidgets import QPushButton, QApplication, QWidget, QVBoxLayout, QStyleOptionButton
from PySide6.QtGui import QIcon, QPixmap
import sys



class tabelButton(QPushButton):

    def __init__(self):

        super().__init__()

        self.setFixedSize(50, 50)

        icon_path = r"ui\buttons\tabelButton\tabel.png"
        icon = QIcon(QPixmap(icon_path))
        self.setIcon(icon)

        self.setIconSize(self.size())

        

        


if __name__ == "__main__":

    app = QApplication(sys.argv)
    with open(r"ui\SpyBot.qss", "r") as file:
        style = file.read()
        app.setStyleSheet(style)  
    window = QWidget()
    layout = QVBoxLayout()
    btn1 = tabelButton()
    window.setLayout(layout)
    layout.addWidget(btn1)
    window.resize(300, 200)
    window.show()
    sys.exit(app.exec())
