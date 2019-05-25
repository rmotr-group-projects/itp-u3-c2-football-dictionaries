from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    players = players_as_dictionaries(squads_list)

    position_dict = {}
    for player in players:
        position_dict.setdefault(player["position"], [])
        position_dict[player["position"]].append(player)
    return position_dict
