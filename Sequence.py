"""importing the random library"""
from random import *

"""class"""
class Sequence:

"""construction method containing three attributes"""
    def __init__(self):
        self.numbers = []
        self.sleep = None
        self.randrange = None

"""method to randomly add a number to the numbers list"""
    def add_random_number(self):
        number = randrange(1, 11)
        self.numbers.append(number)
    
    
        


