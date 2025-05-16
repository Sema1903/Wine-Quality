from sklearn.model_selection import train_test_split
import numpy as np
f = open('winequality-red.csv').read().split('\n')
del f[0]
q = open('winequality-white.csv').read().split('\n')
del q[0]
x = []
y = []
for i in range(len(f)):
    dop = []
    for j in range(len(f[i].split(';'))):
        if f[i].split(';')[j] != '':
            dop.append(float(f[i].split(';')[j]))
        else:
            dop.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    x.append(dop)
    y.append(1)
for i in range(len(q)):
    dop = []
    for j in range(len(q[i].split(';'))):
        if q[i].split(';')[j] != '':
            dop.append(float(q[i].split(';')[j]))
        else:
            dop.append(0)
    x.append(dop)
    y.append(2)
del x[-1]
del y[-1]
scores = []
for i in range(1):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
    from sklearn.neighbors import KNeighborsClassifier
    neigh = KNeighborsClassifier(n_neighbors=3)
    for w in range(len(x_train)):
        print(x_train[w])
    neigh.fit(x_train, y_train)
    s = 0
    for j in range(len(y_test)):
        if y_test[j] == neigh.predict([x_test[j]]):
            s += 1
        scores.append(s/len(y_test))
print(np.mean(scores))