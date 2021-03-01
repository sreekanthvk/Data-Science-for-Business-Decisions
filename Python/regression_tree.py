# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 11:55:24 2021

@author: Sreekanth V K

from https://www.datadriveninvestor.com/2020/04/13/how-do-regression-trees-work/
"""

import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

rng = np.random.RandomState(1)
X = np.sort(5 * rng.rand(80, 1), axis=0)
y = np.sin(X).ravel()
y[::5] += 3 * (0.5 - rng.rand(16))

plt.figure()
plt.xlabel("Dosage (mg)")
plt.ylabel("Efficiency")
plt.scatter(X, y)
plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

# instace for classification
clf = DecisionTreeRegressor(max_depth=2)

# model 
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

plt.figure()
plt.scatter(X_test, y_pred, s=20, edgecolor="black", c="darkorange", label="Observed values")
plt.scatter(X_test, y_test, s=20, edgecolor="black",c="blue", label="Predicted values")
plt.xlabel("Dosage (mg)")
plt.ylabel("Efficiency")
plt.title("Decision Tree Regression")
plt.legend()
plt.show()