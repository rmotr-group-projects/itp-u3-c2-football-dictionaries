from assignment_1 import players_as_dictionaries
from squads_data import SQUADS_DATA
from pprint import pprint


def players_by_position(squads_list):
    positions = []
    positions_list = {}

    for player in squads_list:
        player_position = player.get('position')
        positions.append(player_position)
    
    for position in positions:
        positions_list.setdefault(position, [])

    for player in squads_list:
        player_position = player.get('position')

        for position in positions_list:
            if player_position == position:
                positions_list[player_position].append(player)

    return positions_list

