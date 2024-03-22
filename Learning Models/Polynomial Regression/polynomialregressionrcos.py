# -*- coding: utf-8 -*-
"""polynomialRegressionRCOS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KfDLB9ESqn62hD-HCSLPTIh5atl2On50
"""

#imports
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler

import numpy as np
import math
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

df = pd.read_csv("/content/sandp500.csv")
headers = df.head(0)
print(headers)
df = df.dropna()
df = df.dropna(axis=1)
df= df.dropna(how='all')
numRows = df.shape[0]
df['Date'] = pd.to_datetime(df['Date'])

xDate = df['Date']
xOpen = df[['Open']]
xHigh = df[['High']]
xLow = df[['Low']]
xVol = df[['Volume']]
xClose = df[['Close']]


y = df[['Adj Close']]

#Visualizing open prices to adjusted close price
plt.scatter(xOpen, y)
plt.xlabel('Open Prices')
plt.ylabel('Adjusted Close Prices')
plt.title('Comparison 1')
plt.show()

#Visualizing highest prices to adjusted close price
plt.scatter(xHigh, y)
plt.xlabel('Highest Prices')
plt.ylabel('Adjusted Close Prices')
plt.title('Comparison 2')
plt.show()

#Visualizing lowest prices to adjusted close price
plt.scatter(xLow, y)
plt.xlabel('Lowest Prices')
plt.ylabel('Adjusted Close Prices')
plt.title('Comparison 3')
plt.show()

#Visualizing stock volume to adjusted close price
plt.scatter(xVol, y)
plt.xlabel('Stock Volume')
plt.ylabel('Adjusted Close Prices')
plt.title('Comparison 4')
plt.show()

#Visualizing open price per day
plt.scatter(xDate, xOpen)
plt.xlabel('Date')
plt.ylabel('Opening price')
plt.title('Comparison 5')
plt.show()

#Visualizing closing price per day
plt.scatter(xDate, xClose)
plt.xlabel('Date')
plt.ylabel('Closing price')
plt.title('Comparison 6')
plt.show()

"""After visualizing our data set, we can see that volume stock does not provide a meaningful prediction on our adjusted close prices.
Our models visualizes the stock prices from 2022-01-03 to 2023-12-29, for both data sets.

"""

#Splitting for train test
X = df[['Open', 'High', 'Low']]
xTrain, xTest, yTrain, yTest = train_test_split(X, y, test_size=0.3, random_state=42)

scaler = StandardScaler()
x_train_scaler = scaler.fit_transform(xTrain)
x_test_scaler = scaler.transform(xTest)

lin = LinearRegression()

min_error = 999999
optimalDegree = 1
for degree in range(1, 30):
  poly_features = PolynomialFeatures(degree=degree)
  x_poly_train = poly_features.fit_transform(x_train_scaler)
  x_poly_test = poly_features.transform(x_test_scaler)

  model = LinearRegression()
  model.fit(x_poly_train, yTrain)

  y_pred_train = model.predict(x_poly_train)
  error_train = mean_absolute_error(yTrain, y_pred_train)

  y_pred_test = model.predict(x_poly_test)
  error_test = mean_absolute_error(yTest, y_pred_test)

  if error_test < min_error:
      min_error = error_test
      optimalDegree = degree

print(optimalDegree)
poly = PolynomialFeatures(degree=optimalDegree)
x_poly_train = poly.fit_transform(x_train_scaler)
x_poly_test = poly.transform(x_test_scaler)
poly.fit(x_poly_train, yTrain)
lin.fit(x_poly_train, yTrain)

yPredTrain = lin.predict(x_poly_train)
meanErrorTrain = mean_absolute_error(yTrain, yPredTrain)

yPredTest = lin.predict(x_poly_test)
meanErrorTest = mean_absolute_error(yTest, yPredTest)


print(meanErrorTrain)
print(meanErrorTest)