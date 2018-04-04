from football_dictionaries.assignment_1 import players_as_dictionaries
from football_dictionaries.squads_data import SQUADS_DATA

def players_by_country_and_position(squads_list):
    players_country_dict = {}  #dictionary with countries as keys and values that are dictionaries with position as key and lists of each player as values 
    players_list = players_as_dictionaries(squads_list)  #using players_as_dictionaries(SQUADS_DATA) to access players dictionary
    for player in players_list:
        players_country_dict.setdefault(player['country'], {})  #initialzing players country as keys with values of empty dictionaries
        players_country_dict[player['country']].setdefault(player['position'], [])  #accessing the country value of the country key and initialzing position as key with value of empty list if it doesnt exist
        players_country_dict[player['country']][player['position']].append(player)  #accesing the country value, a dictionary with keys of positions and then accessing the values within this dictionary and appending the player to list
    return players_country_dict
