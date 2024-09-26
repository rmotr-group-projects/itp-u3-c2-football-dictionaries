from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_country_and_position(squads_list):
    expected_countries = {}
    squads_list = players_as_dictionaries(squads_list)
    for player in squads_list:
        country = player['country']
        position = player['position']     
        expected_countries.setdefault(country, {})
        expected_countries[country].setdefault(position,[])
        expected_countries[country][position].append(player)  
    return expected_countries 

