from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    player_dict_list = players_as_dictionaries(squads_list)
    res = {}
    res.setdefault('GK', [])
    res.setdefault('MF', [])
    res.setdefault('FW', [])
    for player in player_dict_list:
        if player['position'] == 'GK':
            res['GK'].append(player)
        if player['position'] == 'FW':
            res['FW'].append(player)
        if player['position'] == 'MF':
            res['MF'].append(player)
    return res