# from assignment_1 import players_as_dictionaries
from football_dictionaries.assignment_1 import players_as_dictionaries
# from squads_data import SQUADS_DATA
from football_dictionaries.squads_data import SQUADS_DATA
from pprint import pprint

def players_by_position(squads_list):
    players = players_as_dictionaries(squads_list)
    goalkeepers = []
    midfielders = []
    forwards = []

    for player in players:
        for key, value in player.items():
            positions = {}
            if value == 'GK':
                goalkeepers.append(player)
            positions['GK'] = goalkeepers
            if value == 'MF':
                midfielders.append(player)
            positions['MF'] = midfielders
            if value == 'FW':
                forwards.append(player)
            positions['FW'] = forwards

    return positions
            

# pprint(players_by_position(SQUADS_DATA))