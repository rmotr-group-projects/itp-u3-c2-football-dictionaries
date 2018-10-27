from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    result = {}
    player_dict = players_as_dictionaries(squads_list)
    for player in player_dict:
        #goal is to put values in result dict of positions
        position = player['position']
        result.setdefault(position, [])
        #goal is to get the player information of that position into the value of the position key
        result[position].append(player)
    return result
