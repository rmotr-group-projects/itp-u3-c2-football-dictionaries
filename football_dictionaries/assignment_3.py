from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_country_and_position(squads_list):
    
    countries = {}
    
    players = players_as_dictionaries(squads_list)
    for player in players:
        position = player['position']
        country = player['country']
        countries.setdefault(country, {})
        countries[country].setdefault(position, [])
        countries[country][position].append(player)
    
    return countries
