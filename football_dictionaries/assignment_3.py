from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_country_and_position(squad):
    players = players_as_dictionaries(squad)
    result = {}
    
    for player in players:
        pos = player['position']
        country = player['country']
        
        result.setdefault(country, {})
        result[country].setdefault(pos, [])
        result[country][pos].append(player)
    
    return result 