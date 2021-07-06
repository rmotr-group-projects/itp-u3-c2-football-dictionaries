from .assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    team = players_as_dictionaries(squads_list)
    by_players_position = {}
    
    for player in team:
        position = player['position']
        by_players_position.setdefault(position, [])
        by_players_position[position].append(player)
    
    return by_players_position
 
