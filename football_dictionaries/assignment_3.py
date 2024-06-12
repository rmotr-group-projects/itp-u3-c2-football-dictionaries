from .assignment_1 import players_as_dictionaries

def players_by_country_and_position(squads_list):
    squad = players_as_dictionaries(squads_list)
    
    sq_country = {}
    
    for player in squad:
        pos = player['position']
        country = player['country']
        
        sq_country.setdefault(country, {})
        sq_country[country].setdefault(pos, [])
        
        sq_country[country][pos].append(player)

    return sq_country
    
    
