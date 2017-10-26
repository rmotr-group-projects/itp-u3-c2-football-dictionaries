from .assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    result ={}
    whole_team = players_as_dictionaries(squads_list)
    for footballers in whole_team:
        position = footballers['position']
        result.setdefault(position, [])
        result[position].append(footballers)
    return result
