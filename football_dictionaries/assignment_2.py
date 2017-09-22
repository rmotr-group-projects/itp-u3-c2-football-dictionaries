from .assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    squad_list = players_as_dictionaries(squads_list)
    squads_by_position = {}
    
    for player in squad_list:
        squads_by_position.setdefault(player['position'], [])
        squads_by_position[player['position']].append(player)
    
    return squads_by_position