from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    result_dict = players_as_dictionaries(squads_list)
    result = {}
    for player in result_dict:
        position = player['position']
        result.setdefault(position,[])
        result[position].append(player)
        
    return result
