import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from design import Ui_MainWindow  # Импортируйте сгенерированный класс

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  # Создайте экземпляр сгенерированного класса
        self.ui.setupUi(self)  # Настройте интерфейс

        # Подключаем кнопки к методам переключения страниц
        self.ui.pushButton_1.clicked.connect(lambda: self.switch_page(0))  # Переключение на первую страницу
        self.ui.pushButton_2.clicked.connect(lambda: self.switch_page(1))  # Переключение на вторую страницу
        self.ui.pushButton_3.clicked.connect(lambda: self.switch_page(2))  # Переключение на третью страницу
        self.ui.pushButton_4.clicked.connect(lambda: self.switch_page(3))  # Переключение на четвертую страницу
        self.ui.pushButton_7.clicked.connect(lambda: self.switch_page(4))  # Переключение на пятую страницу
        self.ui.User.clicked.connect(lambda: self.switch_page(5))  # Переключение на шестую страницу
        self.ui.updateDB.clicked.connect(lambda: self.switch_page(6))  # Переключение на седьмую страницу (если есть)

    def switch_page(self, index):
        """Метод для переключения страниц в stackedWidget."""
        self.ui.stackedWidget.setCurrentIndex(index)
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Загрузка стиля из файла
    with open(r"C:\WorkSpace\Python\projectGSH\ui\SpyBot.qss", "r") as file:
        style = file.read()
        app.setStyleSheet(style)  # Применяем стиль к приложению

    window = MainWindow()  # Создайте экземпляр главного окна
    window.show()  # Отобразите главное окно
    sys.exit(app.exec())  # Запустите главный цикл 