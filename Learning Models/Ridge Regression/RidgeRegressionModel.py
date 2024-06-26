# -*- coding: utf-8 -*-
"""Ridge Regression Model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eQ4UZWcmITOHzIr6mp3yHH3f0owGRZOF#scrollTo=KIZ6SgnSaIp2
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

"""
After visualizing our data set, we can see that volume stock does not provide a meaningful prediction on our adjusted close prices.
Our models visualizes the stock prices from 2022-01-03 to 2023-12-29, for both data sets.
"""

#Testing training of QQQ on S&P500 data
#QQQ
df = pd.read_csv("/content/QQQ.csv")
headers = df.head(0)
print(headers)
df = df.dropna()
df = df.dropna(axis=1)
df= df.dropna(how='all')
numRows = df.shape[0]

xDateQQQ = pd.to_datetime(df['Date'])  # Convert 'Date' column to datetime format
xOpenQQQ = df[['Open']]
xHighQQQ = df[['High']]
xLowQQQ = df[['Low']]
xVolQQQ = df[['Volume']]
xCloseQQQ = df[['Close']]

yQQQ = df[['Adj Close']]

XQQQ = df[['Open', 'High', 'Low']]

print("QQQ DATA SET VISUALIZED")
#Visualizing open prices to adjusted close price
plt.scatter(xOpenQQQ, yQQQ)
plt.xlabel('Open Prices')
plt.ylabel('Adjusted Close Prices')
plt.title('Comparison 1')
plt.show()

#Visualizing highest prices to adjusted close price
plt.scatter(xHighQQQ, yQQQ)
plt.xlabel('Highest Prices')
plt.ylabel('Adjusted Close Prices')
plt.title('Comparison 2')
plt.show()

#Visualizing lowest prices to adjusted close price
plt.scatter(xLowQQQ, yQQQ)
plt.xlabel('Lowest Prices')
plt.ylabel('Adjusted Close Prices')
plt.title('Comparison 3')
plt.show()

#Visualizing stock volume to adjusted close price
plt.scatter(xVolQQQ, yQQQ)
plt.xlabel('Stock Volume')
plt.ylabel('Adjusted Close Prices')
plt.title('Comparison 4')
plt.show()

#Visualizing open price per day
plt.scatter(xDateQQQ, xOpenQQQ)
plt.xlabel('Date')
plt.ylabel('Opening price')
plt.title('Comparison 5')
plt.show()

#Visualizing closing price per day
plt.scatter(xDateQQQ, xCloseQQQ)
plt.xlabel('Date')
plt.ylabel('Closing price')
plt.title('Comparison 6')
plt.show()

#Splitting QQQ data
xTrainQQQ, xTestQQQ, yTrainQQQ, yTestQQQ = train_test_split(XQQQ, yQQQ, test_size=0.3, random_state=42)

#S&P500
df = pd.read_csv("/content/sandp500.csv")
headers = df.head(0)
print(headers)
df = df.dropna()
df = df.dropna(axis=1)
df= df.dropna(how='all')
numRows = df.shape[0]

xDateSP = pd.to_datetime(df['Date'])  # Convert 'Date' column to datetime format
xOpenSP = df[['Open']]
xHighSP = df[['High']]
xLowSP = df[['Low']]
xVolSP = df[['Volume']]
xCloseSP = df[['Close']]

ySP = df[['Adj Close']]

XSP = df[['Open', 'High', 'Low']]

print("S&P500 DATA SET VISUALIZED")
#Visualizing open prices to adjusted close price
plt.scatter(xOpenSP, ySP)
plt.xlabel('Open Prices')
plt.ylabel('Adjusted Close Prices')
plt.title('Comparison 1')
plt.show()

#Visualizing highest prices to adjusted close price
plt.scatter(xHighSP, ySP)
plt.xlabel('Highest Prices')
plt.ylabel('Adjusted Close Prices')
plt.title('Comparison 2')
plt.show()

#Visualizing lowest prices to adjusted close price
plt.scatter(xLowSP, ySP)
plt.xlabel('Lowest Prices')
plt.ylabel('Adjusted Close Prices')
plt.title('Comparison 3')
plt.show()

#Visualizing stock volume to adjusted close price
plt.scatter(xVolSP, ySP)
plt.xlabel('Stock Volume')
plt.ylabel('Adjusted Close Prices')
plt.title('Comparison 4')
plt.show()

#Visualizing open price per day
plt.scatter(xDateSP, xOpenSP)
plt.xlabel('Date')
plt.ylabel('Opening price')
plt.title('Comparison 5')
plt.show()

#Visualizing closing price per day
plt.scatter(xDateSP, xCloseSP)
plt.xlabel('Date')
plt.ylabel('Closing price')
plt.title('Comparison 6')
plt.show()

#Splitting S&P500 data
xTrainSP, xTestSP, yTrainSP, yTestSP = train_test_split(XSP, ySP, test_size=0.3, random_state=42)

ridge = Ridge(alpha=0.1)

#Training QQQ data to ridge regression model
ridge.fit(xTrainQQQ, yTrainQQQ)
#Retraining model based on S&P500 data
ridge.fit(xTrainSP, yTrainSP)

#Predicting S&P500 data
y_test_pred_SP = ridge.predict(xTestSP)

#Predicting QQQ data
y_test_pred_QQQ = ridge.predict(xTestQQQ)

#Finding the MSE values
mse_test_SP = mean_squared_error(yTestSP, y_test_pred_SP)
mse_test_QQQ = mean_squared_error(yTestQQQ, y_test_pred_QQQ)

print('Data Set: DJI', 'MSE Test: ', mse_test_SP)
print('Data Set: QQQ', 'MSE Test: ', mse_test_QQQ)


#Creating model for Tesla
df = pd.read_csv("/content/TSLA-Full.csv")

df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Ensure no missing values in the dataset
df.dropna(inplace=True)

# Define features (X) and target variable (y)
X = df[['Open', 'High', 'Low', 'Volume']]
y = df['Close']

# Split into train and test sets for time series data
train_size = int(0.7 * len(df))
X_train, X_test = X.iloc[:train_size], X.iloc[train_size:]
y_train, y_test = y.iloc[:train_size], y.iloc[train_size:]

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

search=GridSearchCV(estimator=ridge, param_grid={'alpha':np.logspace(-5,2,8)},scoring='neg_mean_squared_error',n_jobs=1,refit=True,cv=10)
search.fit(X,y)
alpha = search.best_params_['alpha']

ridge = Ridge(alpha=.5, random_state=1)

ridge.fit(X_train_scaled, y_train)

y_test_pred = ridge.predict(X_test_scaled)
y_train_pred = ridge.predict(X_train_scaled)

model_test=(mean_squared_error(y_true=y_test, y_pred=y_test_pred))
model_train=(mean_squared_error(y_true=y_train, y_pred=y_train_pred))

#Creates graph to showcase actual data vs predicted
plt.figure(figsize=(10, 6))
plt.plot(df.index[train_size:], y_test, label='Actual Close', marker='o')
plt.plot(df.index[train_size:], y_test_pred, label='Predicted Close', linestyle='--')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.title('Actual vs. Predicted Closing Prices (Test Data)')
plt.legend()
plt.grid(False)
plt.show()

print('Test MSE: ', model_test)
print('Training MSE: ', model_train)