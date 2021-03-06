# -*- coding: utf-8 -*-
"""Copy of Copy of random_forest_classification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1r1PnTVMcq6UV90t9wttsdDiPgkj-dpN4

# Random Forest Classification

## Importing the libraries
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""## Importing the dataset"""

dataset = pd.read_csv('COVID_DATA.csv')
dataset.head()

dataset.shape
# x=dataset['Seve']

dataset.info()

dataset['Severity_Severe'].value_counts()

class0, class1=dataset['Severity_Severe'].value_counts()

severe_0=dataset[dataset['Severity_Severe']==0]
severe_1=dataset[dataset['Severity_Severe']==1]

under_0=severe_0.sample(class1)

under_test=pd.concat([under_0, severe_1])
under_test.head()

under_test['Severity_Severe'].value_counts()

X=under_test.drop(['Severity_Severe'], axis=1)
y=under_test['Severity_Severe']

"""## Splitting the dataset into the Training set and Test set"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, shuffle= 'True', random_state = 45)

print(X_train.shape, y_train.shape)
print(X_test.shape, y_test.shape)

"""## Training the Random Forest Classification model on the Training set"""

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 25, criterion = 'gini',
                                    max_depth=5)
classifier.fit(X_train, y_train)

from sklearn.tree import DecisionTreeClassifier
dt_clf=DecisionTreeClassifier()
dt_clf.fit(X_train, y_train)

"""## Predicting the Test set results"""

from sklearn.neighbors import KNeighborsClassifier
kn_clf=KNeighborsClassifier()
kn_clf.fit(X_train, y_train)

prediction = classifier.predict([[1,0,1,1,1,0,1,1,1,1,0,1]])
print(prediction)

if(prediction == [1]):
  print('YOU HAVE THE POSSIBILITY OF HAVING COVID-19, GET A CT SCAN DONE ASAP')
else:
  print('YOUR SYMPTOMS DO NOT INDICATE COVID-19, TAKE CARE!')

from sklearn.svm import SVC
svc_clf=SVC()
svc_clf.fit(X_train, y_train)

y_pred = svc_clf.predict(X_test)
y_pred
accuracy_score(y_test, y_pred)

# Commented out IPython magic to ensure Python compatibility.
# %%time
# pred1 = classifier.predict(X_test)
# pred2 = dt_clf.predict(X_test)
# pred3 = kn_clf.predict(X_test)
# pred4 = svc_clf.predict(X_test)

from sklearn.ensemble import VotingClassifier
model = VotingClassifier(estimators=[('rf', classifier), ('dt', dt_clf),
                                     ('kn', kn_clf), ('sv', svc_clf)
                                     ], voting='hard')
model.fit(X_train, y_train)
model.score(X_test,y_test)

import xgboost as xgb
xgb_clf=xgb.XGBClassifier(random_state=1,learning_rate=0.01)
xgb_clf.fit(X_train, y_train)
xgb_clf.score(X_test,y_test)

accuracy_score(y_test, y_pred)

"""## Making the Confusion Matrix"""

from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)

from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))