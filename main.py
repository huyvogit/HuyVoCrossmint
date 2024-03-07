'''
Crossmint Coding Challenge
Name: Huy Vo
Github: huyvogit

main.py

This file will run the main program to execute the tasks.
'''

import os
import requests
from polyanet import Polyanet
from soloon import Soloon
from cometh import Cometh

# Get the candidate id from the environment for security purposes
candidate_id =  os.environ.get('CANDIDATE_ID')
api_url = "https://challenge.crossmint.io/api"

#--- Get the goal map for the phase ---
def get_goal():
    map_url = "{api_url}/map/{candidate_id}/goal".format(api_url = api_url, candidate_id = candidate_id)
    try:
        response = requests.get(map_url)
        response.raise_for_status()
        return response.json()['goal']
    except requests.exceptions.RequestException as e:
        print("An error occurred when making request:", e)

#--- Get the characteristic for the astral object if soloon or cometh ---
def get_arg(name):
    return name.lower().split("_")[0]

#--- Match the goal map for the phase ---
def match_goal():
    goal = get_goal()
    if (goal and goal[0]):
        for row in range(len(goal[0])):
            for column in range(len(goal)):
                astral_object = goal[row][column]
                if (astral_object == "POLYANET"):
                    Polyanet(row, column).create_astral_object()
                elif ("SOLOON" in astral_object):
                    Soloon(row, column, get_arg(astral_object)).create_astral_object()
                elif ("COMETH" in astral_object):
                    Cometh(row, column, get_arg(astral_object)).create_astral_object()

if __name__ == "__main__":
    match_goal()
