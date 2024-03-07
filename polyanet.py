'''
Crossmint Coding Challenge
Name: Huy Vo
Github: huyvogit

polyanet.py

This file contains the code for creating and deleting Polyanets.
'''

import requests
import time

class Polyanet:
    #--- Initialize the Polyanet ---
    def __init__(self, row, column):
        self.body = { "candidateId": candidate_id, "row": row, "column": column }

    #--- Create an astral object (defaults to polyanets) ---
    def create_astral_object(self, endpoint = "polyanets"):
        url = "{api_url}/{endpoint}".format(api_url = api_url, endpoint = endpoint)
        try:
            response = requests.post(url, json = self.body)
            response.raise_for_status()
            print("Successfully created a", endpoint[:-1])
        except requests.exceptions.RequestException as e:
            print("An error occurred when making request:", e)
        time.sleep(1)
    
    #--- Delete an astral object (defaults to polyanets) ---
    def delete_astral_object(self, endpoint = "polyanets"):
        url = "{api_url}/{endpoint}".format(api_url = api_url, endpoint = endpoint)
        try:
            requests.delete(url, json = self.body)
            response.raise_for_status()
            print("Successfully deleted a", endpoint[:-1])
        except requests.exceptions.RequestException as e:
            print("An error occurred when making request:", e)
        time.sleep(1)