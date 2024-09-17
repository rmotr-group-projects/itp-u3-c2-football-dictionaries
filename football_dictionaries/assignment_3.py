from assignment_1 import players_as_dictionaries

def players_by_country_and_position(squads_list):
    squads_dict = players_as_dictionaries(squads_list)
    country_and_position = {}
    
    for player in squads_dict:
        country = player['country']
        position = player['position']
        country_and_position.setdefault(country, {}) 
        country_and_position[country].setdefault(position, [])
        country_and_position[country][position].append(player)
            
    return country_and_position 
