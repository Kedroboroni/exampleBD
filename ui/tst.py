import sys
import numpy as np
from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QSizePolicy
"""!!! Таблица со скролом, для просомтра результата"""
class TableDisplay(QWidget):
    def __init__(self, data):
        super().__init__()
        self.setWindowTitle("NumPy Array to Table")
        
        # Создаем QTableWidget
        self.table_widget = QTableWidget()
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.table_widget)

        # Устанавливаем количество строк и столбцов
        self.table_widget.setRowCount(data.shape[0])
        self.table_widget.setColumnCount(data.shape[1])

        # Заполняем таблицу данными из массива NumPy
        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                self.table_widget.setItem(i, j, QTableWidgetItem(str(data[i, j])))

        # Устанавливаем политику размера для прокрутки
        self.table_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Устанавливаем фиксированный размер для таблицы
        #self.table_widget.setFixedSize(400, 300)  # Установите нужный размер

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Пример массива NumPy
    numpy_array = np.random.randint(1, 100, size=(20, 10))  # Пример большого массива
    
    window = TableDisplay(numpy_array)
    #window.resize(400, 300)
    window.show()
    
    sys.exit(app.exec())