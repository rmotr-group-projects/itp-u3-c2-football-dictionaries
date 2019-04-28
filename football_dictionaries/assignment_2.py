from .assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    player_squad = players_as_dictionaries(squads_list)   # from assignment 1
    p_position = {}

    for player in player_squad:
        position = player['position']
        p_position.setdefault(position, [])
        p_position[position].append(player)

    return p_position