from .assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    #convert input to dict(players) with players_as_dictionaries
    #declare dict(result) structure
    #iterate over dict(players) to populate player data based on player['position']
    #return dict(result)
    players = players_as_dictionaries(squads_list)
    result = {
        'GK': [],
        'FW': [],
        'MF': []
    }
    
    for player in players:
        if player['position'] == 'GK':
            result['GK'].append(player)
        elif player['position'] == 'FW':
            result['FW'].append(player)
        elif player['position'] == 'MF':
            result['MF'].append(player)

    return result