# coding: utf-8
"""
py4ds2.py

This is a simple script used for training people new to Python.
"""


## Reading csv files
def read_file(filename):
    line_count = 0
    file_open = open(filename,"r")
    data_array = []
    for line in iter(file_open):
        line_no_newline = line.rstrip()
        line_split = line_no_newline.split(",")
        fn = line_split[0]
        work = line_split[2]
        concat = [fn,work]
        data_array.append(concat)
    return data_array

array1 = read_file("family.csv")
print(array1)

# Regression example in Machine Learning

get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import sklearn

from sklearn.datasets import load_boston
boston = load_boston()

print(boston.feature_names)

"""
Dataset description

00 - CRIM     per capita crime rate by town
01 - ZN       proportion of residential land zoned for lots over 25,000 sq.ft.
02 - INDUS    proportion of non-retail business acres per town
03 - CHAS     Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
04 - NOX      nitric oxides concentration (parts per 10 million)
05 - RM       average number of rooms per dwelling
06 - AGE      proportion of owner-occupied units built prior to 1940
07 - DIS      weighted distances to five Boston employment centres
08 - RAD      index of accessibility to radial highways
09 - TAX      full-value property-tax rate per $10,000
10 - PTRATIO  pupil-teacher ratio by town
11 - B        1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
12 - LSTAT    % lower status of the population
13 - MEDV     (Target) Median value of owner-occupied homes in $1000's

13 X Variables; 1 Y variable

Data Points = 506
"""

bos = pd.DataFrame(boston.data)
bos.describe()

bos.head()

boston.target[:5]

bos['PRICE'] = boston.target

from sklearn.linear_model import LinearRegression
X = bos.drop('PRICE',axis=1)
X[0:5]

bos.PRICE[0:5]

lm = LinearRegression()
lm.fit(X,bos.PRICE)
print(lm.intercept_)
print(lm.coef_)
print ("Number of coefficients is ",len(lm.coef_))

lm.predict(X)[0:5]

plt.scatter(bos.PRICE,lm.predict(X))
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")

mseFull = np.mean((bos.PRICE - lm.predict(X)) ** 2)
print(mseFull)

X[0:2] ## first two data rows

print(boston.target[0:2])

row_1 = [0.00632,18.0,2.31,0.0,0.538,6.575,65.2,4.0900,1.0,296.0,15.3,396.90,4.98]
row_2 = [0.02731,0.0,7.07,0.0,0.469,6.421,78.9,4.9671,2.0,242.0,17.8,396.90,9.14]
tests = [row_1,row_2]
lm.predict(tests)

