from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QLabel, QVBoxLayout, QStackedWidget
"""!!! РАбОТА с вкладками! объеденить с tst.py,чтобы в кладках показывалась значнеие таблицы (запроса с бд)"""
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Создаем горизонтальный макет
        layout = QHBoxLayout()

        # Левый слой с фиксированной шириной
        self.left_widget = QWidget()  # Создаем виджет для левого слоя
        self.left_layer = QVBoxLayout(self.left_widget)
        self.left_widget.setFixedWidth(80)  # Фиксированная ширина 30 пикселей

        # Создаем кнопки и добавляем их в левый слой
        self.buttons = []
        for i in range(5):
            button = QPushButton(f"Кнопка {i + 1}")
            button.clicked.connect(self.on_button_clicked)
            self.left_layer.addWidget(button)
            self.buttons.append(button)

        # Правый слой с QStackedWidget для отображения разных виджетов
        self.right_widget = QStackedWidget()
        self.right_widget.addWidget(self.create_label_widget("Содержимое для кнопки 1"))
        self.right_widget.addWidget(self.create_label_widget("Содержимое для кнопки 3333"))
        self.right_widget.addWidget(self.create_label_widget("Содержимое для кнопки 2"))
        self.right_widget.addWidget(self.create_label_widget("Содержимое для кнопки 3"))
        
        self.right_widget.addWidget(self.create_label_widget("Содержимое для кнопки 5"))

        # Добавляем слои в основной макет
        layout.addWidget(self.left_widget)  # Добавляем виджет с фиксированной шириной
        layout.addWidget(self.right_widget)  # Добавляем QStackedWidget

        self.setLayout(layout)
        self.setWindowTitle("Пример с кнопками и виджетами")

    def create_label_widget(self, text):
        """Создает виджет с меткой."""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        label = QLabel(text)
        layout.addWidget(label)
        widget.setLayout(layout)
        return widget

    def on_button_clicked(self):
        # Получаем индекс нажатой кнопки и переключаем виджет
        button = self.sender()
        print(button)
        index = self.buttons.index(button)
        print(self.buttons)
        self.right_widget.setCurrentIndex(index)  # Переключаем на соответствующий виджет

app = QApplication([])
window = MainWindow()
window.show()
app.exec()



