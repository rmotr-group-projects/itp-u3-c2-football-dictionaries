from .assignment_1 import players_as_dictionaries

def players_by_country_and_position(squads_list):
    '''Input a list of lists where each internal list represents a player
        Use method from assignment_1 to convert to a list of dictionaries where each dictionary represents a player
        Output a dictionary of dictionaries of countries (level 1 key), player positions (level 1 value, level 2 key)
        and players (level 2 values)'''
    squads_dict = players_as_dictionaries(squads_list)
    dict_by_country = {}
    for player in squads_dict:
        country = player['country']
        position = player['position']
        dict_by_country.setdefault(country,{})
        dict_by_country[country].setdefault(position,[])
        dict_by_country[country][position].append(player)
    return dict_by_country