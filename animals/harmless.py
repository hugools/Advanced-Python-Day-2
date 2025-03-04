#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 13:15:29 2025

@author: hugoo
"""

class Birds:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Sparrow', 'Robin', 'Duck']
    def printMembers(self):
        print('Printing harmless members of the Birds class') 
        for member in self.members:
            print('\t%s ' % member)

class Fish:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member fish species
        self.members = ['Salmon', 'Red Snapper', 'Cod']
    def printMembers(self):
        print('Printing harmless members of the Fish class') 
        for member in self.members:
            print('\t%s ' % member)
            
class Mammals:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Sheep', 'Mouse', 'House Cat']
    def printMembers(self):
        print('Printing harmless members of the Mammals class') 
        for member in self.members:
            print('\t%s ' % member)
