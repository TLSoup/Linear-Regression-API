import requests

BASE = "http://127.0.0.1:5000/"

data = [{"cost": 100000, "sqft": 1000, "bdrms": 3, "pool": 0},
        {"cost": 200000, "sqft": 1500, "bdrms": 4, "pool": 0},
        {"cost": 300000, "sqft": 1500, "bdrms": 4.5, "pool": 1},
        {"cost": 257000, "sqft": 1200, "bdrms": 3, "pool": 1}]

for i in range(len(data)):
    response = requests.put(BASE + "listing/" + str(i), data[i])
    print(response.json())