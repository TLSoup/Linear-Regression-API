from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
import response

def regression():
    House_X = []
    Cost_Y = []
    for row in response.json():
        House_X.append([row['sqft'], row['bdrms'], row['pool']])
        Cost_Y.append(row['cost'])
    
    # Split the data into training/testing sets
    House_X_train = House_X[:-20]
    House_X_test = House_X[-20:]

    # Split the targets into training/testing sets
    Cost_Y_train = Cost_Y[:-20]
    Cost_Y_test = Cost_Y[-20:]

    # Create linear regression object
    regr = linear_model.LinearRegression()
    
   # Train the model using the training sets
    regr.fit(House_X_train, Cost_Y_train)

    # Make predictions using the testing set
    Cost_Y_pred = regr.predict(House_X_test)

    # The coefficients
    print('Coefficients: \n', regr.coef_)
    print('offset', regr.intercept_)

    # The mean squared error
    print('Mean squared error: %.2f'
      % mean_squared_error(Cost_Y_test, Cost_Y_pred))

    # The coefficient of determination: 1 is perfect prediction
    print('Coefficient of determination: %.2f'
      % r2_score(Cost_Y_test, Cost_Y_pred))