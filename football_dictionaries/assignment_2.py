# Assignment 1
from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
        players = players_as_dictionaries(squads_list)
        player_dict = {}
        for player in players:
            position = player['position']
            player_dict.setdefault(position, [])
            player_dict[position].append(player)
        return player_dict

