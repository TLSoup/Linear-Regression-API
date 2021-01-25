from flask import Flask
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import requests

app = Flask(__name__)
BASE = "http://127.0.0.1:5000/"

@app.route('/')
def app():

    response = requests.get(BASE + 'listing/0')
    for row in response.json():
        print(row)

# Load the dataset
response = requests.get(BASE + 'listing/0')
X = []
Y = []
for row in response.json():
    X.append([row['sqft'], row['bdrms'], row['pool']])
    Y.append(row['cost'])

# Use only one feature
"""diabetes_X = diabetes_X[:, np.newaxis, 2]

# Split the data into training/testing sets
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

# Split the targets into training/testing sets
diabetes_y_train = diabetes_y[:-20]
diabetes_y_test = diabetes_y[-20:] """

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(X, Y)

# Make predictions using the testing set
#diabetes_y_pred = regr.predict(diabetes_X_test)

# The coefficients
print('Coefficients: \n', regr.coef_)
print('offset', regr.intercept_)

# The mean squared error
""" print('Mean squared error: %.2f'
      % mean_squared_error(diabetes_y_test, diabetes_y_pred))
# The coefficient of determination: 1 is perfect prediction
print('Coefficient of determination: %.2f'
      % r2_score(diabetes_y_test, diabetes_y_pred)) """

# Plot outputs
plt.scatter(X, Y,  color='black')
plt.plot(X, Y, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()
