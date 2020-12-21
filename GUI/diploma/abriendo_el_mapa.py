from matplotlib.image import imread
import pandas as pd
import numpy as np
from time import time

t1 = time()
time
def converting_to_normal_data(list, index):
    return np.array([[j[index] for j in i] for i in list])

def getting_nice_data(image, color):
    total = np.array([])
    line = converting_to_normal_data(image, color)
    for elements in line:
        total = np.concatenate((total, elements))

    return pd.Series(total.astype(int))

titan = np.array(imread(r'C:\Users\Admin\Desktop\diploma\imagenes de prueba\venus.png'))
a3 = np.array([[[10, 11, 12], [13, 14, 15], [16, 17, 18]],
               [[20, 21, 22], [23, 24, 25], [26, 27, 28]],
               [[30, 31, 32], [33, 34, 35], [36, 37, 38]]])


df1 = pd.DataFrame({"R": getting_nice_data(titan, 0),
                   "G": getting_nice_data(titan, 1),
                   "B": getting_nice_data(titan, 2)})

df1['altura'] = 1

df2 = pd.DataFrame({"R": getting_nice_data(a3, 0),
                   "G": getting_nice_data(a3, 1),
                   "B": getting_nice_data(a3, 2)})

df2['altura'] = 3
dfr = pd.concat([df1, df2])
t2 = time()
print(dfr)
print(t2 - t1)