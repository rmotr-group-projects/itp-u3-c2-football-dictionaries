from pprint import pprint
from squads_data import SQUADS_DATA as squad;
from assignment_1 import players_as_dictionaries

def players_by_country_and_position(squads_list):
    # create containers outside the loop which will be filled with values from inside the loop
    countries = dict()
    positions = dict()
    
    # create the list of players as dictionaries - we've already done this in assignment 1
    players = players_as_dictionaries(squads_list)
    
    # loop over every player in the unsorted dictionary
    for player in players: 
        # for each player's country, create a dictionary with keys for each value if it does not exist with an empty dictionary as the value
        countries.setdefault(player['country'], {} )
        # for each of the countries we just created, fill the empty dictionary with each position if it does not exist with an empty list as the value
        countries[player['country']].setdefault(player['position'], [] )
        # when player (from for player in players) matches the 'country' and 'position' keys created, add that player to the list
        countries[player['country']][player['position']].append(player)
    return countries