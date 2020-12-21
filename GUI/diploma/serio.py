from matplotlib.image import imread
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd
import os
from time import time

x_train = list()
y_train = list()
titan = imread(r'C:\Users\Admin\Desktop\diploma\imagenes de prueba\titan.jpg')
path = r'D:\ANACONDA_PROYECTS\Diploma\imagenes de prueba\partes de la legenda'
for file in os.listdir(path):
    legend = imread(path + '\\' + file)
    for i in range(legend.shape[0]):
        for j in range(legend.shape[1]):
            x_train.append(legend[i][j])
            y_train.append(int(file[:-4]))
t1 = time()
model = RandomForestClassifier(n_estimators=100)
model.fit(x_train, y_train)
t2 = time()
leyenda = imread(r'D:\ANACONDA_PROYECTS\Diploma\imagenes de prueba\titan_legend.jpg')
print(len(x_train), leyenda.shape[0] * leyenda.shape[1], len(y_train))
print('tiempo para entrenar y calcular: ', t2 - t1)
