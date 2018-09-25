

from random import randint


class Die():
    def __init__(self,number=6):
        self.number=number


    def roll(self):
        return randint(1,self.number)
