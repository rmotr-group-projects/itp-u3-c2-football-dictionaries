from football_dictionaries.assignment_1 import players_as_dictionaries
from football_dictionaries.assignment_1 import transform_list_player_to_dict


def players_by_position(squads_list):
    positions_dict = {}
    for player in players_as_dictionaries(squads_list):
        if player["position"] not in positions_dict.keys():
            positions_dict.setdefault(player['position'], [player])
        else:
            positions_dict[player["position"]].append(player)

    return positions_dict
