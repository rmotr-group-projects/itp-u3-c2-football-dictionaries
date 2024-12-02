from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_country_and_position(squads_list):
            
    player_list = players_as_dictionaries(squads_list)
    
    country_dict = {}
        
    for player in player_list:
                        
        country = player['country']
        country_dict.setdefault(country, {})
        
        position_dict = {}
                   
        position = player['position']
        position_dict.setdefault(position, [])

        position_dict[position].append(player)
        
        if position in country_dict[country].keys():
            country_dict[country][position].append(player)
        
        else:
            country_dict[country].update(position_dict)


        
        
        
        
    return country_dict
        
        



        
            
            
        