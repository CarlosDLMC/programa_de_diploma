from interface_1 import Ui_Dialog
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from matplotlib.image import imread
from sklearn.ensemble import RandomForestClassifier
from openpyxl import Workbook
import numpy as np
import os
import traceback

file_path = ''
folder_path = ''
got_file = False
got_directory = False
threadpool = QThreadPool()
app = QApplication(sys.argv)
Dialog = QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()
ui.label_3.setText("Выбирайте, пожалуйста, карту")

def get_file():
    global file_path
    global got_file
    path = f"{ui.browse_image()[0]}"
    palabras = path.split('/')
    for part in palabras:
        file_path += part
        if part != palabras[-1]:
            file_path += '\\'
    ui.label.setText(f"{palabras[-1]}")
    if path != '':
        got_file = True
    if got_file and got_directory:
        ui.label_3.setText("Данные готовы к анализу!")
    else:
        ui.label_3.setText("Выбирайте, пожалуйста, легенду")

def get_directory():
    global folder_path
    global got_directory
    path = f"{ui.browse_folder()}"
    folder_path = path
    ui.label_2.setText(f"{path}")
    if path != '':
        got_directory = True
    if got_file and got_directory:
        ui.label_3.setText("Данные готовы к анализу!")
    else:
        ui.label_3.setText("Выбирайте, пожалуйста, карту")

def modeling(progress_callback):
    ui.label_3.setText('Пожалуйста, подождите')
    global got_file
    global got_directory
    if got_file and got_directory:
        count = 0
        progress = 0
        global file_path
        global folder_path
        wb = Workbook()
        dest_filename = 'result.xlsx'
        ws1 = wb.active
        ws1.append([])
        ws1.append(['координаты каждой точки и их высоты'])
        ws1.append([])
        line = list()
        for i in range(181):
            line += ['долгота', 'широта', 'высота', '\t']
        ws1.append(line)
        x_train = list()
        y_train = list()
        x_pixel = 0
        y_pixel = 0
        data = list()
        height = 0
        titan = imread(str(file_path))

        for file in os.listdir(folder_path):
            legend = imread(folder_path + '\\' + file)
            for i in range(legend.shape[0]):
                for j in range(legend.shape[1]):
                    x_train.append(legend[i][j])
                    y_train.append(int(file[:-4]))

        model = RandomForestClassifier(n_estimators=100)
        model.fit(x_train, y_train)

        dx = (titan.shape[1] - 1) / 359
        dy = (titan.shape[0] - 1) / 180

        
        for y_degree in range(90, -91, -2):
            line.clear()
            for x_degree in range(-180, 180, 2):
                data = [titan[int(y_pixel), int(x_pixel)]]
                height = model.predict(data)[0]
                line += [x_degree, y_degree, height, '\t']
                x_pixel += dx
                print(line)
            count += 1
            progress = count / 91
            progress_callback.emit(progress)
            ws1.append(line)        
            y_pixel += dy
            x_pixel = 0
        wb.save(filename = dest_filename)

def progress_fn(percent):
    ui.label_3.setText(f'Прогресс: {percent * 100:.2f}%')

class WorkerSignals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(float)


class Worker(QRunnable):
    def __init__(self, function, *args, **kwargs):
        super(Worker, self).__init__()
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        self.kwargs['progress_callback'] = self.signals.progress         

    @pyqtSlot()
    def run(self):
        try:
            self.function(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit('success')  
        finally:
            self.signals.finished.emit()  

def thread_complete():
    global got_file
    global got_directory
    global file_path
    global directory_path
    if got_file and got_directory:
        got_file = False
        got_directory = False
        file_path = ''
        directory_path = ''
        ui.label.setText("")
        ui.label_2.setText("")
        ui.label_3.setText('Результаты готовы!')
    else:
        ui.label_3.setText('Сначала, введите все данные')
    

def analyce():
    worker = Worker(modeling) 
    # worker.signals.result.connect(self.print_output)
    worker.signals.finished.connect(thread_complete)
    worker.signals.progress.connect(progress_fn)
    threadpool.start(worker) 

ui.pushButton_2.clicked.connect(get_directory)
# ui.pushButton.clicked.connect(ui.browse)
ui.pushButton.clicked.connect(get_file)
# ui.pushButton.clicked.connect(ui.get_image)
ui.pushButton_3.clicked.connect(analyce)
sys.exit(app.exec_())