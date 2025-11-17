from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtGui import QPixmap, QPen, QStandardItemModel,QStandardItem
from PySide6.QtMultimedia import QSoundEffect, QMediaPlayer
from PySide6.QtCore import  QUrl, QModelIndex, QTime, QDate
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
        model.setItem(index.row(),1,QStandardItem(ui_window.event_time.text()))
    if type=='Дата':
        model.setItem(index.row(),2,QStandardItem(ui_window.event_date.selectedDate()))

def row_killer():
    index = ui_window.event_list.currentIndex()
    model.removeRow(index.row())

def on_row_selected(current:QModelIndex):
    if not current.isValid():
        return
    row = current.row()
    time = QTime.fromString(model.item(row,1).text(),"HH:mm")
    date = QDate.fromString(model.item(row,1).text(),"d MMM")
    name = model.item(row, 0)

    ui_window.event_name.setText(name.text())
    ui_window.event_time.setTime(time)
    ui_window.event_date.setSelectedDate(date)
model=QStandardItemModel(0, 3)
ui_window=Ui_MainWindow()
app=QApplication()
window=QMainWindow()

ui_window.setupUi(window)

ui_window.event_list.setModel(model)
ui_window.event_list.selectionModel().currentChanged.connect(on_row_selected)
ui_window.event_list.setSelectionBehavior(ui_window.event_list.SelectionBehavior.SelectRows)

ui_window.delete_button.clicked.connect(row_killer)
ui_window.event_name.textChanged.connect(lambda: data_change("Событие"))
ui_window.event_time.timeChanged.connect(lambda: data_change("Время"))
model.setHorizontalHeaderLabels(['Событие','Время','Дата'])

ui_window.event_list.setColumnWidth(0,159)
ui_window.event_list.setColumnWidth(1,159)
ui_window.event_list.setColumnWidth(2,159)

ui_window.add_button.clicked.connect(lambda: row_adder('Новый год','23:00','31 декабря'))
window.setWindowIcon(QPixmap('icon.png'))
window.setWindowTitle("Todolist")

window.show()
app.exec()
