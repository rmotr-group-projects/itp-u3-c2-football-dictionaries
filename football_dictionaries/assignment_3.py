from football_dictionaries.assignment_1 import players_as_dictionaries

def player_sort(country_dict, player, country, position):
    if player['country'] == country:
            if player['position'] == position:
                if position not in country_dict[country].keys():
                    country_dict[country].setdefault(position, [])
                country_dict[country][position].append(player)
    return country_dict

def players_by_country_and_position(squads_list):
    country_dict = {}
    position_list = ['GK', 'FW', 'MF']
    country_list = ['Argentina', 'Brazil', 'Belgium', 'South Korea']
    for country in country_list:
        country_dict.setdefault(country, {})
    #country_dict.setdefault('Argentina, {})
    #country_dict.setdefault('Brazil, {})
    #country_dict.setdefault('Belgium, {})
    #country_dict.setdefault('South Korea, {})
    player_dict_list = players_as_dictionaries(squads_list)
    for player in player_dict_list:
        for country in country_list:
            for position in position_list:
                country_dict = player_sort(country_dict, player, country, position)
        # if player['country'] == 'Argentina':
        #     if player['position'] == 'GK':
        #         if 'GK' not in country_dict['Argentina'].keys():
        #             country_dict['Argentina'].setdefault('GK', [])
        #         country_dict['Argentina']['GK'].append(player)
        #     elif player['position'] == 'FW':
        #         if 'FW' not in country_dict['Argentina'].keys():
        #             country_dict['Argentina'].setdefault('FW', [])
        #         country_dict['Argentina']['FW'].append(player)
        #     elif player['position'] == 'MF':
        #         if 'MF' not in country_dict['Argentina'].keys():
        #             country_dict['Argentina'].setdefault('MF', [])
        #         country_dict['Argentina']['MF'].append(player)
        # elif player['country'] == 'Brazil':
        #     if player['position'] == 'GK':
        #         if 'GK' not in country_dict['Brazil'].keys():
        #             country_dict['Brazil'].setdefault('GK', [])
        #         country_dict['Brazil']['GK'].append(player)
        #     elif player['position'] == 'MF':
        #         if 'MF' not in country_dict['Brazil'].keys():
        #             country_dict['Brazil'].setdefault('MF', [])
        #         country_dict['Brazil']['MF'].append(player)
        #     elif player['position'] == 'FW':
        #         if 'FW' not in country_dict['Brazil'].keys():
        #             country_dict['Brazil'].setdefault('FW', [])
        #         country_dict['Brazil']['FW'].append(player)
        # elif player['country'] == 'Belgium':
        #     if player['position'] == 'GK':
        #         if 'GK' not in country_dict['Belgium'].keys():
        #             country_dict['Belgium'].setdefault('GK', [])
        #         country_dict['Belgium']['GK'].append(player)
        #     elif player['position'] == 'MF':
        #         if 'MF' not in country_dict['Belgium'].keys():
        #             country_dict['Belgium'].setdefault('MF', [])
        #         country_dict['Belgium']['MF'].append(player)
        #     elif player['position'] == 'FW':
        #         if 'FW' not in country_dict['Belgium'].keys():
        #             country_dict['Belgium'].setdefault('FW', [])
        #         country_dict['Belgium']['FW'].append(player)
        # elif player['country'] == 'South Korea':
        #     if player['position'] == 'GK':
        #         if 'GK' not in country_dict['South Korea'].keys():
        #             country_dict['South Korea'].setdefault('GK', [])
        #         country_dict['South Korea']['GK'].append(player)
        #     elif player['position'] == 'MF':
        #         if 'MF' not in country_dict['South Korea'].keys():
        #             country_dict['South Korea'].setdefault('MF', [])
        #         country_dict['South Korea']['MF'].append(player)
        #     elif player['position'] == 'FW':
        #         if 'FW' not in country_dict['South Korea'].keys():
        #             country_dict['South Korea'].setdefault('FW', [])
        #         country_dict['South Korea']['FW'].append(player)
    return country_dict
                