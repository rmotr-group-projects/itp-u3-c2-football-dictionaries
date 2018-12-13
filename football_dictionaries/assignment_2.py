from .assignment_1 import *

def players_by_position(data):
    result = {}
    position_keys = []
    player_dictionaries = players_as_dictionaries(data)
    for player in player_dictionaries:
        if player['position'] not in position_keys:
            position_keys.append(player['position'])

    for positon_key in position_keys:
        player_list =[]
        for player in player_dictionaries:
            if player['position'] == positon_key:
                player_list.append(player)
        result[positon_key] = player_list
    return result
