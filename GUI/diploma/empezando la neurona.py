from sklearn.ensemble import RandomForestClassifier
from matplotlib.image import imread
import numpy as np
from time import time

t1 = time()
titan = imread(r'C:\Users\Admin\Desktop\diploma\imagenes de prueba\titan.jpg')
x_train = list()
y_train = list()
t2 = time()
for i in range(titan.shape[0]):
    for j in range(titan.shape[1]):
        x_train.append(titan[i][j])
        y_train.append(1000)
t3 = time()
model = RandomForestClassifier(n_estimators=100)
model.fit(x_train, y_train)
t4 = time()
for i in range(16000):
    pronost = model.predict([[i % 255, 255, 255]])

t5 = time()
print(pronost)
print('lectura de imagen: ', t2 - t1, ' segundos')
print('preparacion de datos:', t3 - t2, ' segundos')
print('entrenamiento del modelo: ', t4 - t3, ' segundos')
print('pronostico: ', t5 - t4, ' segundos')

