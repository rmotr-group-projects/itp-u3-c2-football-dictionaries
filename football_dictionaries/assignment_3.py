from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_country_and_position(squads_list):
    result={}
    football_list=players_as_dictionaries(squads_list)
    
    for player in football_list:
        country=player['country']
        result.setdefault(country,{})
        position=player['position']
        result[country].setdefault(position,[])
        result[country][position].append(player)
        
    return result