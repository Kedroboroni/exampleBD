import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from window import MainWindow
from ex import Widget


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    wid = Widget(QMainWindow)
    window.show()
    sys.exit(app.exec())
