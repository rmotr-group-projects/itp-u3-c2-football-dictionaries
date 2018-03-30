from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_country_and_position(squads_list):
    result = {}
    
    for player in players_as_dictionaries(squads_list):
 
        result.setdefault(player['country'], [])
        result.setdefault(player['position'], [])
        result[player['country']['position']].append(player)
    
    return result

"""
Example pseudo code from Jason Symons

for player
    select country
    select posiition
    result[country][position] = player
    """