from football_dictionaries.assignment_1 import players_as_dictionaries

# def player_sort(country_dict, player, country, position):
#     if player['country'] == country:
#             if player['position'] == position:
#                 if position not in country_dict[country].keys():
#                     country_dict[country].setdefault(position, [])
#                 country_dict[country][position].append(player)
#     return country_dict

def players_by_country_and_position(squads_list):
    country_dict = {}
    player_dict_list = players_as_dictionaries(squads_list)
    for player in player_dict_list:
        country = player['country']
        position = player['position']
        country_dict.setdefault(country, {})
        country_dict[country].setdefault(position, [])
        country_dict[country][position].append(player)
    # position_list = ['GK', 'FW', 'MF']
    # country_list = ['Argentina', 'Brazil', 'Belgium', 'South Korea']
    # for country in country_list:
    #     country_dict.setdefault(country, {})
    # for player in player_dict_list:
    #     for country in country_list:
    #         for position in position_list:
    #             country_dict = player_sort(country_dict, player, country, position)
    return country_dict
                