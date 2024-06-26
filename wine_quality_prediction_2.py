# -*- coding: utf-8 -*-
"""Wine quality prediction .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wL0V0icjiyxtiW6iBajWdLSfaDqqjIG9
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

wine=pd.read_csv('winequality-red.csv')

wine.sample(40)

wine.info()

wine.describe()

wine.isnull().sum()

plt.figure(figsize = (12,6))
sns.scatterplot(wine['density'])
plt.show()

plt.figure(figsize = (12,6))
sns.scatterplot(wine['volatile acidity'])
plt.show()

wine['fixed acidity'].plot(kind ='box')

wine.hist(figsize=(10,10),bins=50)
plt.show()

wine.sample(5)

wine['density'].unique()

wine['fixed acidity'].unique()

wine['volatile acidity'].unique()

# Separate depedent and indepedent variables
X = wine.drop(['density','volatile acidity'], axis = 1)
Y = wine['volatile acidity']

X

print(Y)

from sklearn.model_selection import train_test_split

wine.head()

X = wine.drop(['quality'], axis = 1)
y = wine['quality']

X.head()

y

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

model_res=pd.DataFrame(columns=['Model', 'Score'])

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score

wine_data = pd.read_csv('winequality-red.csv')

X = wine_data.drop('density', axis=1)
y = wine_data['quality']

X = wine_data.drop('fixed acidity', axis=1)
y = wine_data['quality']

X

y



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

sgd_clf = SGDClassifier(loss="log", max_iter=1000, tol=1e-3, random_state=42)
sgd_clf.fit(X_train_scaled, y_train)

y_pred = sgd_clf.predict(X_test_scaled)

y_pred

# Accuracy evaluation
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Load the wine quality dataset
wine_data = pd.read_csv('winequality-red.csv')

X = wine_data.drop('density', axis=1)
y = wine_data['quality']

X = wine_data.drop('fixed acidity', axis=1)
y = wine_data['quality']

X

y

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

svc_clf = SVC(kernel='linear', random_state=42)
svc_clf.fit(X_train_scaled, y_train)

y_pred = svc_clf.predict(X_test_scaled)

y_pred

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

wine_data = pd.read_csv('winequality-red.csv')

X = wine_data.drop('density', axis=1)
y = wine_data['quality']

X = wine_data.drop('fixed acidity', axis=1)
y = wine_data['quality']

X

y

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf_clf = RandomForestClassifier(n_estimators=100, random_state=42)
rf_clf.fit(X_train, y_train)

y_pred = rf_clf.predict(X_test)

y_pred

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

