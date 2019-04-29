from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_country_and_position(squads_list):
    result = {}
    players_dict = players_as_dictionaries(squads_list)

    players_by_country = {}
    for player in players_dict:
        players_by_country.setdefault(player['country'], [])
        players_by_country[player['country']].append(player)
    
    for country, player_set in players_by_country.items():
        players_by_position = {}
        for player in player_set:
            players_by_position.setdefault(player['position'], [])
            players_by_position[player['position']].append(player)
        result[country] = players_by_position
    
    return result