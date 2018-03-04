from squads_data import SQUADS_DATA
from assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    # Reassign the list to new variable to be safe
    postions_list = squads_list
    # Empty dictionary that will be returned
    players_dict = {
        'GK': [],
        'MF': [],
        'FW': []
        
    }
    
    # Pass the new assigned list to dictionary function from assignment_1 and loop through
    for player in players_as_dictionaries(postions_list):
        # Look for 'GK' position
        if player['position'] == 'GK':
            # Append player to 'GK' key
            players_dict['GK'].append(player)
        
        # Look for 'MF' position
        if player['position'] == 'MF':
            # Append player to 'MF' key
            players_dict['MF'].append(player)
        
        # Look for 'FW' position
        if player['position'] == 'FW':
            # Append player to 'FW' key
            players_dict['FW'].append(player)
            
    return players_dict

#players_by_position(SQUADS_DATA)