# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QStackedWidget, QStatusBar, QTabWidget, QTableView,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(799, 452)
        self.centralwidget = QWidget(MainWindow)

        self.sidebartWidget = QWidget(self.centralwidget)

        self.sidebartWidget.setGeometry(QRect(0, 0, 61, 411))
        self.pushButton_1 = QPushButton(self.sidebartWidget)

        self.pushButton_1.setGeometry(QRect(10, 10, 41, 41))
        self.pushButton_2 = QPushButton(self.sidebartWidget)

        self.pushButton_2.setGeometry(QRect(10, 50, 41, 41))
        self.pushButton_3 = QPushButton(self.sidebartWidget)

        self.pushButton_3.setGeometry(QRect(10, 90, 41, 41))
        self.pushButton_4 = QPushButton(self.sidebartWidget)

        self.pushButton_4.setGeometry(QRect(10, 130, 41, 41))
        self.User = QPushButton(self.sidebartWidget)

        self.User.setGeometry(QRect(10, 370, 41, 41))
        self.updateDB = QPushButton(self.sidebartWidget)

        self.updateDB.setGeometry(QRect(10, 330, 41, 41))
        self.pushButton_7 = QPushButton(self.sidebartWidget)

        self.pushButton_7.setGeometry(QRect(10, 170, 41, 41))
        self.generalWidget = QWidget(self.centralwidget)
        self.generalWidget.setGeometry(QRect(60, 0, 741, 321))
        self.stackedWidget = QStackedWidget(self.generalWidget)
        self.stackedWidget.setGeometry(QRect(0, 0, 731, 321))
        self.page = QWidget()
        self.tabWidget = QTabWidget(self.page)
        self.tabWidget.setGeometry(QRect(10, 10, 721, 301))
        self.tab = QWidget()
        self.tableView = QTableView(self.tab)
        self.tableView.setGeometry(QRect(0, 0, 341, 271))
        self.label = QLabel(self.tab)
        self.label.setGeometry(QRect(370, 10, 331, 251))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.label_3 = QLabel(self.tab_2)
        self.label_3.setGeometry(QRect(370, 10, 331, 251))
        self.tableView_3 = QTableView(self.tab_2)
        self.tableView_3.setGeometry(QRect(0, 0, 341, 271))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.label_4 = QLabel(self.tab_3)
        self.label_4.setGeometry(QRect(370, 10, 331, 251))
        self.tableView_4 = QTableView(self.tab_3)
        self.tableView_4.setGeometry(QRect(0, 0, 341, 271))
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.label_5 = QLabel(self.tab_4)
        self.label_5.setGeometry(QRect(370, 10, 331, 251))
        self.tableView_5 = QTableView(self.tab_4)

        self.tableView_5.setGeometry(QRect(0, 0, 341, 271))
        self.tabWidget.addTab(self.tab_4, "")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()

        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.stackedWidget.addWidget(self.page_6)
        self.console = QWidget(self.centralwidget)
        self.console.setGeometry(QRect(60, 320, 731, 91))
        self.progressBar = QProgressBar(self.console)

        self.progressBar.setGeometry(QRect(0, 60, 118, 23))
        self.progressBar.setValue(24)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 799, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)
        self.tabWidget.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.User.setText(QCoreApplication.translate("MainWindow", u"User", None))
        self.updateDB.setText(QCoreApplication.translate("MainWindow", u"DB", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"tab1", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"tab2", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"tab3", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"tab4", None))
    # retranslateUi

