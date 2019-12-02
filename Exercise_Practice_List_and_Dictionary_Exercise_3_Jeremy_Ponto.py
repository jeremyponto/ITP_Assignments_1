# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 17:00:48 2019

@author: user
"""

groceries = [
        "banana",
        "orange",
        "apple"
        ]
stocks = {
        "banana": 6,
        "apple": 0,
        "orange": 32,
        "pear": 15
        } 
prices = {
        "banana": 4,
        "apple": 2,
        "orange": 1.5,
        "pear": 3
        }
def compute_bill(food):
    total = 0
    for item in food:
        if stocks[item] != 0:
            total += prices[item]
            stocks[item] -= 1
    return total
print(compute_bill(groceries))