from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_country_and_position(squads_list):
    squads_dict = players_as_dictionaries(squads_list)
    
    players_by_country_and_positions_dict = {}
    
    for squad in squads_dict:
        country = squad['country']
        players_by_country_and_positions_dict.setdefault(country, {})
        
    for country in players_by_country_and_positions_dict:
        players_by_position_dict = {}
        
        for squad in squads_dict:
            if country == squad['country']:
                if squad['position'] not in players_by_position_dict:
                    players_by_position_dict[squad['position']] = [squad] 
                else:
                    players_by_position_dict[squad['position']].append(squad)
        players_by_country_and_positions_dict[country] = players_by_position_dict
    
    return players_by_country_and_positions_dict
 
 