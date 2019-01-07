from .assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    player_position = {}
    squad = players_as_dictionaries(squads_list)
    
    for player in squad:
        position = player["position"]
        player_position.setdefault(position, [])
        player_position[position].append(player)
    return player_position
