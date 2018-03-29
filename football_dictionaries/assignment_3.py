from .assignment_1 import players_as_dictionaries

def players_by_country_and_position(squads_list):
    #Function modifies assignment_2 function and returns dictionary by country
    new_squads_list = players_as_dictionaries(squads_list)
    country_dict = {
        'Argentina': None,
        'Belgium': None,
        'Brazil': None,
        'South Korea': None
    }
    for country in country_dict:
        player_position_dict = {}
        for player in new_squads_list:       
            if player['country'] == country:
                player_position_dict.setdefault(player['position'], [])
                player_position_dict[player['position']].append(player)
        country_dict[country] = player_position_dict
    return country_dict