from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    result = {
        'GK': [],
        'MF': [],
        'FW': [],
    }
    GK_list = result["GK"]
    MF_list = result["MF"]
    FW_list = result["FW"]
    players = players_as_dictionaries(squads_list)
    
    for player in players:
        if player['position'] == 'GK':
            GK_list.append(player)
        elif player['position'] == 'MF':
            MF_list.append(player)
        else:
            FW_list.append(player)
    return result
            