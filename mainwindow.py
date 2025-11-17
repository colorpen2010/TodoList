# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QHeaderView, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableView, QTextBrowser, QTimeEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(497, 722)
        MainWindow.setMinimumSize(QSize(497, 722))
        MainWindow.setMaximumSize(QSize(497, 722))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.add_button = QPushButton(self.centralwidget)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setGeometry(QRect(10, 410, 75, 24))
        self.delete_button = QPushButton(self.centralwidget)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setGeometry(QRect(150, 410, 75, 24))
        self.event_name = QLineEdit(self.centralwidget)
        self.event_name.setObjectName(u"event_name")
        self.event_name.setGeometry(QRect(10, 440, 111, 22))
        self.event_date = QCalendarWidget(self.centralwidget)
        self.event_date.setObjectName(u"event_date")
        self.event_date.setGeometry(QRect(240, 400, 256, 190))
        self.event_time = QTimeEdit(self.centralwidget)
        self.event_time.setObjectName(u"event_time")
        self.event_time.setGeometry(QRect(10, 470, 111, 22))
        self.event_desc = QTextBrowser(self.centralwidget)
        self.event_desc.setObjectName(u"event_desc")
        self.event_desc.setGeometry(QRect(10, 600, 481, 71))
        self.event_list = QTableView(self.centralwidget)
        self.event_list.setObjectName(u"event_list")
        self.event_list.setGeometry(QRect(10, 10, 481, 381))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 497, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.add_button.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.delete_button.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.event_time.setDisplayFormat(QCoreApplication.translate("MainWindow", u"HH:mm", None))
    # retranslateUi

