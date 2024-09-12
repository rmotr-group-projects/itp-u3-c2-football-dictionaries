def players_by_position(squads_list):
    result = {
        'GK': [],
        'FW': [],
        'MF': [],
    }
    
    for player in squads_list:
        new_player = {
            'caps': player[4],
            'club': player[5],
            'club_country': player[7],
            'country': player[6],
            'date_of_birth': player[3],
            'name': player[2],
            'number': player[0],
            'position': player[1],
            'year': player[8],
        }
        
        position = new_player['position']
        
        if position == 'GK':
            result['GK'].append(new_player)
        if position == 'MF':
            result['MF'].append(new_player)
        if position == 'FW':
            result['FW'].append(new_player)
    return result
