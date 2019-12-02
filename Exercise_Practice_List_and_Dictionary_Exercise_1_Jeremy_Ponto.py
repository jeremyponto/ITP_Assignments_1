# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 16:57:19 2019

@author: user
"""

inventory = {
        'gold' : 500,
        'pouch' : [
                'flint',
                'twine',
                'gemstone'
                ],
        'backpack' : [
                'xylophone',
                'dagger',
                'bedroll',
                'bread loaf'
                ]
        }
print(inventory)
inventory['pocket'] = [
        'seashell',
        'strange berry',
        'lint'
        ]
print(inventory)
inventory['backpack'].sort()
print(inventory)
inventory['backpack'].remove('dagger')
print(inventory)
inventory['gold'] += 50
print(inventory)