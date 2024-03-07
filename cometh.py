'''
Crossmint Coding Challenge
Name: Huy Vo
Github: huyvogit

cometh.py

This file contains the code for creating and deleting Comeths.
'''

from polyanet import Polyanet

class Cometh(Polyanet):
    #--- Initialize the Cometh and add direction ---
    def __init__(self, row, column, direction):
        super().__init__(row, column)
        self.body["direction"] = direction

    #--- Create a cometh ---
    def create_astral_object(self):
        super().create_astral_object("comeths")
    
    #--- Delete a cometh ---
    def delete_astral_object(self):
        super().delete_astral_object("comeths")