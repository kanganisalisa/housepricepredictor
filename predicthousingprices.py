# -*- coding: utf-8 -*-
"""PredictHousingPrices.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NQ9ctKkDbD_FupU0oDCdxfg4-Cws1iHf

Import Libraries, Create Dataframe:
"""

import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns #python library for data visualization

from sklearn.datasets import fetch_california_housing
housing = fetch_california_housing()

#print(housing.keys())
#print(housing.data)
#print(housing.target)
#etc

#pandas dataframe for creating a copy of the dataset
df = pd.DataFrame(housing.data, columns=housing.feature_names)
df['MEDV'] = housing.target

#use df.head() to see first five rows of dataframe
#use df.tail() to see last five rows of the created dataframe
#use df.dtype or df.info to know data type various features present in the dataset
#use df.isnull().sum() to check for missing values in each column

df.describe()

"""Visualizing Data: Boxplot, Heatmap, Density"""

df.boxplot()

corr = df.corr()
sns.heatmap(corr)

sns.kdeplot(data=df, x="MEDV")

"""Training Model:"""

#select elements to train model on
x1 = df[['MedInc','HouseAge','AveRooms','AveBedrms','Population','AveOccup','Latitude','Longitude']]
y1 = df['MEDV']

#create train and test sets
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x1, y1, test_size =0.33,random_state = 5)

"""Use Regression on Model:"""

from sklearn.linear_model import LinearRegression
from sklearn import metrics
regressor = LinearRegression()
regressor.fit(x_train, y_train)
y_pred = regressor.predict(x_test)
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
df

metrics.mean_absolute_error(y_test, y_pred)
metrics.mean_squared_error(y_test, y_pred)
np.sqrt(metrics.mean_squared_error(y_test, y_pred))
metrics.r2_score(y_test, y_pred)

"""Linear Regression, AveRooms to predict MEDV:"""

x1 = np.array(x_test['AveRooms'])
y1 = np.array(y_pred)
model = np.polyfit(x1, y1, 1)
a, b = model

plt.scatter(x1, y1)

plt.plot(x_test['AveRooms'], (a*x_test['AveRooms'] + b))
plt.plot(x_test['AveRooms'], y_pred,'o')
plt.xlabel("Average Num of Rooms")
plt.ylabel("Median Value")

"""Linear Regression, HouseAge to predict MEDV"""

x1 = np.array(x_test['HouseAge'])
y1 = np.array(y_pred)
model = np.polyfit(x1, y1, 1)
a, b = model

plt.scatter(x1, y1)

plt.plot(x_test['HouseAge'], (a*x_test['HouseAge'] + b))
plt.plot(x_test['HouseAge'], y_pred,'o')
plt.xlabel("House Age")
plt.ylabel("Median Value")

"""Linear Regression, Latitude to predict MEDV:"""

x1 = np.array(x_test['Latitude'])
y1 = np.array(y_pred)
model = np.polyfit(x1, y1, 1)
a, b = model

plt.scatter(x1, y1)

plt.plot(x_test['Latitude'], (a*x_test['Latitude'] + b))
plt.plot(x_test['Latitude'], y_pred,'o')
plt.xlabel("Latitude")
plt.ylabel("Median Value")

"""Linear Regression, Longitude to predict MEDV:"""

x1 = np.array(x_test['Longitude'])
y1 = np.array(y_pred)
model = np.polyfit(x1, y1, 1)
a, b = model

plt.scatter(x1, y1)

plt.plot(x_test['Longitude'], (a*x_test['Longitude'] + b))
plt.plot(x_test['Longitude'], y_pred,'o')
plt.xlabel("Longitude")
plt.ylabel("Median Value")

sns.lmplot(x="Longitude", y="MEDV", data=df);

"""Pairplot:"""

df = pd.DataFrame(housing.data, columns=housing.feature_names)
df['MEDV'] = housing.target
p = sns.pairplot(df, x_vars=['MedInc','HouseAge','AveRooms','AveBedrms','Population','AveOccup','Latitude','Longitude'], y_vars=['MEDV'], height=4, aspect=0.8, kind='reg')
p.set(ylim = (0,5))