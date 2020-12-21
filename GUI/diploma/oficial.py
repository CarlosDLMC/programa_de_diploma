from matplotlib.image import imread
from sklearn.ensemble import RandomForestClassifier
from openpyxl import Workbook
import numpy as np
import pandas as pd
import os
from time import time

t1 = time()
wb = Workbook()
dest_filename = 'Titan_test4.xlsx'
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
ceros = 0
titan = imread(r'D:\ANACONDA_PROYECTS\Diploma\mapas\titan_map.jpg')
path = r'D:\ANACONDA_PROYECTS\Diploma\imagenes de prueba\partes de la legenda'

for file in os.listdir(path):
    legend = imread(path + '\\' + file)
    for i in range(legend.shape[0]):
        for j in range(legend.shape[1]):
            x_train.append(legend[i][j])
            y_train.append(int(file[:-4]))

model = RandomForestClassifier(n_estimators=100)
model.fit(x_train, y_train)

dx = (titan.shape[1] - 1) / 359
dy = (titan.shape[0] - 1) / 180

count_positive = 0
count_negative = 0
maximum = 0
for y_degree in range(90, -91, -2):
    line.clear()
    for x_degree in range(-180, 180, 2):
        data = [titan[int(y_pixel), int(x_pixel)]]
        height = model.predict(data)[0]
        if height > 0:
            print(x_degree, y_degree, height)
            count_positive += 1
        elif height == 0:
            ceros += 1
        else:
            count_negative += 1
        if height > maximum:
            maximum = height
        line += [x_degree, y_degree, height, '\t']
        x_pixel += dx
    ws1.append(line)
    y_pixel += dy
    x_pixel = 0


wb.save(filename = dest_filename)

t2 = time()
print(t2 - t1)
print('negativos: ', count_negative, ' positivos: ', count_positive, ' ceros: ', ceros)
print('maximo:' , maximum)

