# EI-Interview

Set up a restful API on a local webserver that performs linear regression using an artificial neural network on the following dataset to generate a cost estimation function from a set of (cost, test sample) pairs shown below


Cost	Square footage	Bedrooms	Swimming Pool
100,000	    1000	       3	        No
200,000	    1500	       4	        No
300,000	    1500	       4.5	        Yes
257,000 	1200	       3	        Yes


The RESTfull API should receive a .JSON containing a numpy array-like structure that matches the table above and it should return a four parameter weight matrix (x, y, z, offset) used to estimate cost from the other three variables. cost = sqft * x + beds * y + pool * z + offset

The linear regression should be performed in python. The API can be set up in any language.

STEPS TO COMPLETE:

1. Finish your React so that the data is sent to your Python endpoint (POST)
2. Update your Regression logic to return the results of the regression
3. In React, when the regression data has been recieved (as a result of your fetch statement), then display the data. HINT: useState is going to be your friend