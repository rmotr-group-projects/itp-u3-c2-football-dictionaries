from .assignment_1 import players_as_dictionaries

def players_by_country_and_position(squads_list):
    
    country_list = {}
    
    for player in players_as_dictionaries(squads_list):
        position = player['position']
        country = player['country']    
        
        country_list.setdefault(country, {})
        country_list[country].setdefault(position, [])
        #access the list to append the player.
        country_list[country][position].append(player)
        
       

    return country_list
        