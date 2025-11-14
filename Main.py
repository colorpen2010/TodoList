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

def data_change(type):
    """
    :param type: в type лежит тип изменяемого объекта, пример: name,x,y.
    """
    index=ui_window.event_list.currentIndex()
    if type=='Событие':
        model.setItem(index.row(),0,QStandardItem(ui_window.event_name.text()))
    if type=='Время':
        model.setItem(index.row(),1,QStandardItem(str(ui_window.timeEdit.value())))

model=QStandardItemModel(0, 3)
ui_window=Ui_MainWindow()
app=QApplication()
window=QMainWindow()

ui_window.setupUi(window)

ui_window.event_list.setModel(model)

ui_window.event_name.textChanged.connect(lambda: data_change("Событие"))

model.setHorizontalHeaderLabels(['Событие','Время','Дата'])

ui_window.event_list.setColumnWidth(0,159)
ui_window.event_list.setColumnWidth(1,159)
ui_window.event_list.setColumnWidth(2,159)

ui_window.add_button.clicked.connect(lambda: row_adder('Новый год','23:00','31 декабря'))
window.setWindowIcon(QPixmap('icon.png'))
window.setWindowTitle("Todolist")

window.show()
app.exec()
