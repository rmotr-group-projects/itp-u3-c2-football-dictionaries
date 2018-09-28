from .assignment_1 import players_as_dictionaries

def players_by_country_and_position(squads_list):
    player_dict = players_as_dictionaries(squads_list)
    countries = {}
    
    for player in player_dict:
        countries.setdefault(player['country'], {})
        countries[player['country']].setdefault(player['position'], [])
        
        print('-------')
        print(countries)
        
        thisCountry = countries[player["country"]]
        thisCountry[player['position']].append(player)
        
        # countries[player['country']['position']].append(player)
    return countries