""" EXAMPLE
In this file you can find sample data for applying
the TrafficFlowMod class in model.py file
"""

graph = [
    ("5", ["7", "9"]),
    ("6", ["7", "8"]),
    ("7", ["8", "10"]),
    ("8", ["11", "12"]),
    ("9", ["10", "16"]),
    ("10", ["11", "13"]),
    ("11", ["14"]),
    ("12", ["15"]),
    ("13", ["14", "16"]),
    ("14", ["15", "17"]),
    ("15", []),
    ("16", ["17"]),
    ("17", [])
]

O = ["5", "6"]
D = ["15", "17"]

demand = [6000, 6750, 7500, 5250]

capacity = [3600] * 19

free_time = [
    10, 10, 
    10, 14.1,
    10, 10,
    10, 14.1,
    10, 22.4,
    10, 10,
    10,
    10,
    10, 10,
    10, 10,
    10
]