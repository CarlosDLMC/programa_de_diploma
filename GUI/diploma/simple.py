from sklearn.ensemble import RandomForestClassifier
import numpy as np

np.random.seed(1)
X = [[0, 0, 1], [1, 1, 0], [1, 0, 0], [0, 1, 1]]
Y = [0, 1, 1, 0]
Z = [[1, 0, 1], [0, 0, 0]]
model = RandomForestClassifier(n_estimators=100)
clf = model.fit(X, Y)
pronost = model.predict(Z)
print(pronost)
