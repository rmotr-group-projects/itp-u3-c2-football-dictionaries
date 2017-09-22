from .assignment_1 import players_as_dictionaries
  
  
def players_by_position(squads_list):
    as_dict = players_as_dictionaries(squads_list)
    dict_by_position = {}
    for player in as_dict:
        pos = player['position']
        dict_by_position.setdefault(pos, [])
        dict_by_position[pos].append(player)
    
    return dict_by_position