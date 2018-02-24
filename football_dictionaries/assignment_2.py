from .assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    position_dict = players_as_dictionaries(squads_list)
    player_position = {}
    for player in position_dict:
        pos = player["position"]
        player_position.setdefault(pos, [])
        player_position[pos].append(player)
    return player_position    
        
      
    
