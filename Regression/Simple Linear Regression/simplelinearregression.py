#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 01:03:30 2019

@author: rey10
"""


#Importing the Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

#Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

#Splitting the dataset into Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

#Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""

#Fitting Simple Linear Regression to the Training Set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

#Predicting the Test set Results
y_pred = regressor.predict(X_test)

#Visualising the Training set results
plt.scatter(X_train, y_train ,color ="red")
plt.plot(X_train,regressor.predict(X_train),color="blue")
plt.title("Salary vs Experience(Training Set)")
plt.xlabel("Years of Experienced")
plt.ylabel("Salary")
plt.show()

#Visualising the Test set results
plt.scatter(X_test, y_test ,color ="red")
plt.plot(X_train,regressor.predict(X_train),color="blue")
plt.title("Salary vs Experience(Test Set)")
plt.xlabel("Years of Experienced")
plt.ylabel("Salary")
plt.show()