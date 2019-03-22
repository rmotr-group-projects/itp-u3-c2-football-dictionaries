from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    result = {
        'GK' : [],
        'MF' : [],
        'FW' : [],
        }
    p_dic = players_as_dictionaries(squads_list)
    for player in p_dic:
        if player['position'] == 'GK':
            result['GK'].append(player)
        if player['position'] == 'MF':
            result['MF'].append(player)
        if player['position'] == 'FW':
            result['FW'].append(player)
    return result