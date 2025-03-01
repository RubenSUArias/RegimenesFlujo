"""
Created on Fri Aug 21 16:14:37 2020
clasifica según los regímenes de flujo pero sin una vision adecuada

@author: Ruben
"""
import numpy as np 
import joblib
B=np.loadtxt('trainingDATA.txt')
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test=train_test_split(B[:,0:4], B[:,4], test_size=0.2)
from sklearn.linear_model import LogisticRegression 
model=LogisticRegression(solver='lbfgs', multi_class="ovr")
model.fit(X_train, y_train)
joblib.dump(model, "FluxRegimes.pkl")