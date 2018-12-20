from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    current_players = players_as_dictionaries(squads_list)
    player_position_dict = {
        'GK': [],
        'MF': [],
        'FW': []
    }
    
    # loop through current players
    # if current player not in player_position_dict, add them by position
    
    for player in current_players:
        # append players by position
        if (player['position'] == 'GK') and (player not in player_position_dict['GK']):
            player_position_dict['GK'].append(player)
        elif (player['position'] == 'DF') and (player not in player_position_dict['DF']):
            player_position_dict['DF'].append(player)
        elif (player['position'] == 'MF') and (player not in player_position_dict['MF']):
            player_position_dict['MF'].append(player)
        elif (player['position'] == 'FW') and (player not in player_position_dict['FW']):
            player_position_dict['FW'].append(player)
    
    
    return player_position_dict
