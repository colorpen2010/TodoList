from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtGui import QPixmap, QPen, QStandardItemModel,QStandardItem
from PySide6.QtMultimedia import QSoundEffect, QMediaPlayer
from PySide6.QtCore import  QUrl
from mainwindow import Ui_MainWindow

def row_adder(event,time,date):
    row = [
        QStandardItem(str(event)),
        QStandardItem(str(time)),
        QStandardItem(str(date))
    ]
    model.appendRow(row)

model=QStandardItemModel(0, 3)
ui_window=Ui_MainWindow()
app=QApplication()
window=QMainWindow()

ui_window.setupUi(window)

ui_window.event_list.setModel(model)

model.setHorizontalHeaderLabels(['Событие','Время','Дата'])

ui_window.add_button.clicked.connect(lambda: row_adder('Новый год','23:00','31 декабря'))
window.setWindowIcon(QPixmap('icon.png'))
window.setWindowTitle("Todolist")

window.show()
app.exec()
