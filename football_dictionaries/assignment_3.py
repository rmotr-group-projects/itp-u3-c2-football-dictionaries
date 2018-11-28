from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_country_and_position(squads_list):
    squads_dict = players_as_dictionaries(squads_list)
    result_dict = {}
 
    for squad in squads_dict:
        player_country = squad['country']
        player_position = squad['position']
        result_dict.setdefault(player_country, {})
        result_dict[player_country].setdefault(player_position, [])
        result_dict[player_country][player_position].append(squad)
    return result_dict