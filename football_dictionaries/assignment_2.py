# Assignment 1
from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    new_squad_list = players_as_dictionaries(squads_list)
    by_position = {}
    
    for player in new_squad_list:
        position = player['position']
        by_position.setdefault(position, [])
        by_position[position].append(player)

    return by_position
