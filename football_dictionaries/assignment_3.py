from football_dictionaries.assignment_1 import players_as_dictionaries
def players_by_country_and_position(squads_list):
    players = players_as_dictionaries(squads_list)
    new_dict = {}
    
    for player in players:
        country = player['country']
        position = player['position'] 
        new_dict.setdefault(country, {})
        new_dict[country].setdefault(position, [])
        new_dict[country][position].append(player)
        
    return new_dict
    
    
    
        

        