from PySide6.QtWidgets import QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QLabel, QSizePolicy
#from widgets import организовывают располл, Sidebar, MessageArea

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Мое приложение")
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout(central_widget)  # Основной вертикальный лейаут
        
        # Боковая панель
        self.sidebar = Sidebar(self.on_sidebar_button_click)
        main_layout.addWidget(self.sidebar)
        
        # Основная рабочая область
        self.tab_widget = CustomTabWidget()
        self.tab_widget.hide()  # Скрываем вкладки по умолчанию
        main_layout.addWidget(self.tab_widget)
        
        # Горизонтальный лейаут для кнопок и основного лейбла
        bottom_layout = QHBoxLayout()
        
        # Основной лейбл для кнопок 2, 3, 4
        self.main_label = QLabel("Выберите вкладку")
        self.main_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  # Устанавливаем политику размера
        self.main_label.setFixedHeight(40)  # Устанавливаем фиксированную высоту
        bottom_layout.addWidget(self.sidebar)  # Добавляем боковую панель с кнопками
        bottom_layout.addWidget(self.main_label)  # Добавляем основной лейбл
        
        main_layout.addLayout(bottom_layout)  # Добавляем горизонтальный лейаут в основной

        # Область сообщений внизу
        self.message_area = MessageArea()
        main_layout.addWidget(self.message_area)

    def on_sidebar_button_click(self, tab_name):
        
        if tab_name == "Вкладка 1":
            self.tab_widget.show()  # Показываем вкладки только для первой кнопки
            self.main_label.hide()  # Скрываем основной лейбл
        else:
            self.tab_widget.hide()  # Скрываем вкладки для остальных кнопок
            self.main_label.setText(f"Вы открыли {tab_name}")  # Обновляем текст основного лейбла
            self.main_label.show()  # Показываем основной лейбл
        
        self.message_area.append_message(f"Открыта {tab_name}")

