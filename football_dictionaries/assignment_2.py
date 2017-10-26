from assignment_1 import players_as_dictionaries
from squads_data import SQUADS_DATA

def players_by_position(squads_list):
    player_position = {}
    for player in players_as_dictionaries(squads_list):
        if player["position"] not in player_position:
            player_position.update({player["position"]:[]})
            player_position[player['position']].append(player)           
        else:
            player_position[player['position']].append(player)
    return player_position