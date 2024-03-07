'''
Crossmint Coding Challenge
Name: Huy Vo
Github: huyvogit

soloon.py

This file contains the code for creating and deleting Soloons.
'''

from polyanet import Polyanet

class Soloon(Polyanet):
    #--- Initialize the Soloon and add color ---
    def __init__(self, row, column, color):
        super().__init__(row, column)
        self.body["color"] = color

    #--- Create a soloon ---
    def create_astral_object(self):
        super().create_astral_object("soloons")
    
    #--- Delete a soloon ---
    def delete_astral_object(self):
        super().delete_astral_object("soloons")