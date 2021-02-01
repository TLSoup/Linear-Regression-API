from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
import requests

BASE = "http://127.0.0.1:5000/"

def linear_regression():
    response = requests.get(BASE + 'listings')
    for row in response.json():
       print(row)

    House_X = []
    Cost_Y = []
    for row in response.json():
        House_X.append([row['sqft'], row['bdrms'], row['pool']])
        Cost_Y.append([row['cost']])
    
    # Split the data into training/testing sets
    House_X_train = House_X[:]
    House_X_test = House_X[:]

    # Split the targets into training/testing sets
    Cost_Y_train = Cost_Y[:]
    Cost_Y_test = Cost_Y[:]

    # Create linear regression object
    regr = linear_model.LinearRegression()
    
    # Train the model using the training sets
    regr.fit(House_X_train, Cost_Y_train)

    # Make predictions using the testing set
    Cost_Y_pred = regr.predict(House_X_test)

    # The coefficients
    print('Coefficients: \n', regr.coef_)
    print('offset', regr.intercept_)
        
    # The coefficient of determination: 1 is perfect prediction
    print('Coefficient of determination: %.2f'
    % r2_score(Cost_Y_test, Cost_Y_pred))

    # The mean squared error
    print('Mean squared error: %.2f'
    % mean_squared_error(Cost_Y_test, Cost_Y_pred))

linear_regression()