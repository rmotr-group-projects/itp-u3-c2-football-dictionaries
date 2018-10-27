from football_dictionaries.assignment_1 import players_as_dictionaries

def position_sort(position_dict, player, position):
    if player['position'] == position:
        position_dict[position].append(player)
    return position_dict

def players_by_position(squads_list):
    player_dict_list = players_as_dictionaries(squads_list)
    position_list = ['GK', 'FW', 'MF']
    position_dict = {}
    for position in position_list:
        position_dict.setdefault(position, [])
    # res.setdefault('GK', [])
    # res.setdefault('MF', [])
    # res.setdefault('FW', [])
    for player in player_dict_list:
        for position in position_list:
            position_dict = position_sort(position_dict, player, position)
        # if player['position'] == 'GK':
        #     position_dict['GK'].append(player)
        # if player['position'] == 'FW':
        #     position_dict['FW'].append(player)
        # if player['position'] == 'MF':
        #     position_dict['MF'].append(player)
    return position_dict