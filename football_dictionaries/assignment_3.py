from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_country_and_position(squads_list):
    new_list = players_as_dictionaries(squads_list)
    country_dict = {}
 
    for player in new_list:
        country = player['country']
        pos = player['position']
    
        country_dict.setdefault(country,{})
        country_dict[country].setdefault(pos,[])
        country_dict[country][pos].append(player)
     
    return country_dict
    pass
