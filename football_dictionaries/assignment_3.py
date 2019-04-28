from .assignment_1 import players_as_dictionaries

def players_by_country_and_position(squads_list):
    player_squad = players_as_dictionaries(squads_list)   # from assignment 1
    p_country = {}
       

    for player in player_squad:
        position = player['position']
        country = player["country"]
        
        p_country.setdefault(country, {})
        p_country[country].setdefault(position, [])
        
        p_country[country][position].append(player)

    return p_country






