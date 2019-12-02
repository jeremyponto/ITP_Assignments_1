# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 17:00:44 2019

@author: user
"""

prices = {
        "banana": 4,
        "apple": 2,
        "orange": 1.5,
        "pear": 3
        }
stocks = {
        "banana": 3,
        "apple": 0,
        "orange": 1,
        "pear": 2
        }
for item in prices:
    print(item + "\nprice: " + str(prices[item]) + "\nstock: " + str(stocks[item]))
total = 0
for item in prices:
    total += prices[item] * stocks[item]
print(total)