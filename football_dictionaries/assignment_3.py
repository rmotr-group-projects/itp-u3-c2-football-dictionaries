from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_country_and_position(squads_list):
    squads_dict = players_as_dictionaries(squads_list)
    result = {}
    
    for squad in squads_dict:
        position = squad['position']
        country = squad['country']
        result.setdefault(country , {})
        result[country].setdefault(position,[])
        result[country][position].append(squad)
    
    return result
