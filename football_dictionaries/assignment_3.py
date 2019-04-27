from .assignment_1 import players_as_dictionaries

def players_by_country_and_position(squads_list):
    
    squads_data = players_as_dictionaries(squads_list)
    
    players_by_pos_country = {}
    
    for player in squads_data:
        
        country = player['country']
        position_abr = player['position']
        
        players_by_pos_country.setdefault(country, {})
        players_by_pos_country[country].setdefault(position_abr, [])
        players_by_pos_country[country][position_abr].append(player)
        
    return players_by_pos_country
    
