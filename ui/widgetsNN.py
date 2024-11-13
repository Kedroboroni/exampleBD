from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QTabWidget, QLabel, QTextEdit

class CustomTabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.addTab(self.create_tab_content(1), "Вкладка 1")
        self.addTab(self.create_tab_content(2), "Вкладка 2")
        self.addTab(self.create_tab_content(3), "Вкладка 3")
        self.addTab(self.create_tab_content(4), "Вкладка 4")

    def create_tab_content(self, tab_number):
        """Создает содержимое для вкладки с номером tab_number."""
        tab_content = QWidget()
        layout = QVBoxLayout()
        label = QLabel(f"Этот лейбл из вкладки {tab_number}")
        layout.addWidget(label)
        tab_content.setLayout(layout)
        return tab_content

class Sidebar(QWidget):
    def __init__(self, on_button_click):
        super().__init__()
        layout = QVBoxLayout()
        button1 = QPushButton("Вкладка 1")
        button2 = QPushButton("Вкладка 2")
        button3 = QPushButton("Вкладка 3")
        button4 = QPushButton("Вкладка 4")
        
        button1.clicked.connect(lambda: on_button_click("Вкладка 1"))
        button2.clicked.connect(lambda: on_button_click("Вкладка 2"))
        button3.clicked.connect(lambda: on_button_click("Вкладка 3"))
        button4.clicked.connect(lambda: on_button_click("Вкладка 4"))
        
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)
        
        self.setLayout(layout)

class MessageArea(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Сообщения:")
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(False)
        
        layout.addWidget(self.label)
        layout.addWidget(self.text_edit)
        
        self.setLayout(layout)

    def append_message(self, message):
        self.text_edit.append(message)
