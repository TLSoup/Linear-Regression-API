# EI-Interview

Set up a restful API on a local webserver that performs linear regression using an artificial neural network on the following dataset to generate a cost estimation function from a set of (cost, test sample) pairs shown below


Cost	Square footage	Bedrooms	Swimming Pool
100,000	    1000	       3	        No
200,000	    1500	       4	        No
300,000	    1500	       4.5	        Yes
257,000 	1200	       3	        Yes


The RESTfull API should receive a .JSON containing a numpy array-like structure that matches the table above and it should return a four parameter weight matrix (x, y, z, offset) used to estimate cost from the other three variables. cost = sqft * x + beds * y + pool * z + offset

The linear regression should be performed in python. The API can be set up in any language.
