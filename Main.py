from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PySide6.QtGui import QPixmap, QPen, QStandardItemModel,QStandardItem
from PySide6.QtMultimedia import QSoundEffect, QMediaPlayer
from PySide6.QtCore import  QUrl, QModelIndex, QTime, QDate
from mainwindow import Ui_MainWindow
from form import Ui_Form

def row_adder(event,time,date):
    row = [
        QStandardItem(str(event)),
        QStandardItem(str(time)),
        QStandardItem(str(date)),
        QStandardItem("Описание")
    ]
    model.appendRow(row)
    ui_window.event_list.hideColumn(3)


def data_change(type):
    """
    :param type: в type лежит тип изменяемого объекта, пример: name,x,y.
    """
    index=ui_window.event_list.currentIndex()
    if type=='Событие':
        model.setItem(index.row(),0,QStandardItem(ui_window.event_name.text()))
    if type=='Время':
        times=ui_window.event_time.time().toString('H:m:s')
        model.setItem(index.row(),1,QStandardItem(times))
    if type=='Дата':
        dates=ui_window.event_date.selectedDate().toString('d MMMM yyyy')
        model.setItem(index.row(),2,QStandardItem(dates))
    if type=='Описание':
        descs=ui_window.event_desc.toPlainText()
        model.setItem(index.row(),3,QStandardItem(descs))

def row_killer():
    index = ui_window.event_list.currentIndex()
    model.removeRow(index.row())

def on_row_selected(current:QModelIndex):
    if not current.isValid():
        return
    row = current.row()
    time = QTime.fromString(model.item(row,1).text(),"HH:mm")
    date = QDate.fromString(model.item(row,2).text(),"d MMMM yyyy")
    name = model.item(row, 0)
    description= model.item(row,3)
    ui_window.event_desc.setText(description.text())
    ui_window.event_name.setText(name.text())
    ui_window.event_time.setTime(time)
    ui_window.event_date.setSelectedDate(date)
model=QStandardItemModel(0, 3)
ui_window=Ui_MainWindow()
ui_widget=Ui_Form()
app=QApplication()
window=QMainWindow()
widged=QWidget()

ui_widget.setupUi(widged)
ui_window.setupUi(window)

ui_window.event_list.setModel(model)
ui_window.event_list.hideColumn(3)
ui_window.event_list.selectionModel().currentChanged.connect(on_row_selected)
ui_window.event_list.setSelectionBehavior(ui_window.event_list.SelectionBehavior.SelectRows)

ui_window.delete_button.clicked.connect(row_killer)
ui_window.event_name.textChanged.connect(lambda: data_change("Событие"))
ui_window.event_time.timeChanged.connect(lambda: data_change("Время"))
ui_window.event_date.selectionChanged.connect(lambda: data_change("Дата"))
ui_window.event_desc.textChanged.connect(lambda: data_change("Описание"))
model.setHorizontalHeaderLabels(['Событие','Время','Дата'])

ui_window.event_list.setColumnWidth(0,159)
ui_window.event_list.setColumnWidth(1,159)
ui_window.event_list.setColumnWidth(2,159)

print()

ui_window.add_button.clicked.connect(lambda: row_adder('Новый год','23:00','31 December 2025'))

window.setWindowIcon(QPixmap('icon.png'))
window.setWindowTitle("Todolist")

widged.show()
window.show()
app.exec()
