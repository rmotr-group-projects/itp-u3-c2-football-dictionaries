from squads_data import SQUADS_DATA
from assignment_1 import players_as_dictionaries

data = players_as_dictionaries(SQUADS_DATA)

def players_by_position(squads_list):
    positions = {}
    for player in data:
        position = player['position']
        if position not in positions:
            positions[position] = []
        positions[position].append(player)
    return positions
