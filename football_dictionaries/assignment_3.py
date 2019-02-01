from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_country_and_position(squads_list):
    players_dicts = players_as_dictionaries(squads_list)
    res = {}
    for player in players_dicts:
        country = player['country']
        position = player['position']
        res.setdefault(country,{})
        
        res[country].setdefault(position,[])
        
        res[country][position].append(player)
        
    return res
