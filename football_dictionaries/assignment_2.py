from .assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    player_dict = players_as_dictionaries(squads_list)
    positions = {}
    for player in player_dict:
        positions.setdefault(player['position'], [])
        positions[player['position']].append(player)
    return positions
