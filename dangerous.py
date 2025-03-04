#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 13:16:05 2025

@author: hugoo
"""

class Birds:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Eagle', 'Hawk', 'Falcon']
    def printMembers(self):
        print('Printing dangerous members of the Birds class') 
        for member in self.members:
            print('\t%s ' % member)

class Fish:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member fish species
        self.members = ['Stingray', 'Tiger Shark', 'Catfish']
    def printMembers(self):
        print('Printing dangerous members of the Fish class') 
        for member in self.members:
            print('\t%s ' % member)
            
class Mammals:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Tiger', 'Elephant', 'Wild Cat']
    def printMembers(self):
        print('Printing dangerous members of the Mammals class') 
        for member in self.members:
            print('\t%s ' % member)