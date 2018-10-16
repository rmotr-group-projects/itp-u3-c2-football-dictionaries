from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    squads_dict = players_as_dictionaries(squads_list)
    result = {}
    
    for squad in squads_dict:
        position = squad['position']
        result.setdefault(position,[])
        result[position].append(squad)
    return result

