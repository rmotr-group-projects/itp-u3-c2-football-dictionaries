from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    positions = {
        'GK': [],
        'MF': [],
        'FW': []
    }
    players = players_as_dictionaries(squads_list)
    for player in players:
        if player['position'] == 'MF':
            positions['MF'].append(player)
        elif player['position'] == 'FW':
            positions['FW'].append(player)
        elif player['position'] == 'GK':
            positions['GK'].append(player)
    return positions