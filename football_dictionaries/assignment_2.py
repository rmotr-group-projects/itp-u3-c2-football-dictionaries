from .assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    squad = players_as_dictionaries(squads_list)
    on_position = {}
    for player in squad:
        position = player['position']
        on_position.setdefault(position, [])
        on_position[position].append(player)
    return on_position
