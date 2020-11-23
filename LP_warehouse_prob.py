from pulp import * 

# Creates a list of all the supply nodes
Warehouses = ["A","B"]

# Creates a dictionary for the number of units of supply for each supply node
supply = {"A": 1000,
        "B": 4000}

# Creates a list of all demand nodes
Bars = ["1", "2", "3", "4", "5"]

# Creates a dictionary for the number of units of demand for each demand node
demand = {"1": 500,
        "2": 900,
        "3": 1800,
        "4": 200,
        "5": 700}