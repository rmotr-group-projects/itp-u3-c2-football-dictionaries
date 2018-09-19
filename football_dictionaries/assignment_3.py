from football_dictionaries.assignment_2 import players_by_position

def players_by_country_and_position(squads_list):
    
    position_dict = players_by_position(squads_list)
    
    country_pos_dict = {}
    
    for position_key, player_list in position_dict.items():
        
        for player in player_list:
            
            country_key = player['country']
            
            if country_key in country_pos_dict:
                
                country_dict = country_pos_dict[country_key]
                
            else:
                
                country_pos_dict[country_key] = {}
                country_dict = country_pos_dict[country_key]
                
            if position_key in country_dict:
                    
                country_dict[position_key].append(player)
                    
            else:
                    
                country_dict[position_key] = [player]
                
    return country_pos_dict
                    
            
    
    
