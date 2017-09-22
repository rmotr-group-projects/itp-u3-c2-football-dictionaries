from .assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    players_in_pos_dict = {}
    
    players_in_dict_list = players_as_dictionaries(squads_list)
    
    for player in players_in_dict_list:
        position = player["position"]
        
        if players_in_pos_dict.get(position) == None:
            players_list = [player]
            players_in_pos_dict[position] = players_list
        else:
            players_in_pos_dict[position].append(player)
    
    return players_in_pos_dict