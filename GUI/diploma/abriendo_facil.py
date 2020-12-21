import numpy as np
from matplotlib.image import imread

titan = np.array(imread(r'C:\Users\Admin\Desktop\diploma\imagenes de prueba\titan.jpg'))
print(titan.shape)
sueltas = list()
y = list()
for i in range(titan.shape[0]):
    for j in range(titan.shape[1]):
        sueltas.append(titan[i][j])
        y.append(1000)
print(1494 * 2128)
print(len(sueltas))
print(len(y))
for k in range(1200000, 1200021):
    print(sueltas[k])