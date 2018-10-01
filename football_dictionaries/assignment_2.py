def players_as_dictionaries(squads_list):
    
    players_as_dict = []
    
    for player in squads_list:
        
        player_dict = {
            'number': player[0],
            'position': player[1],
            'name': player[2],
            'date_of_birth': player[3],
            'caps': player[4],
            'club': player[5],
            'country': player[6],
            'club_country': player[7],
            'year': player[8],
            
        }
        
        players_as_dict.append(player_dict)
    return players_as_dict
#-------------------------------------------------------------------------------
def players_by_position(squads_list):
    
    '''so we want a dictionary and each key in the dictionary
    will be a list of player dictionaries
    '''
    
    # This will give me a list with each player as a dictionary
    
    players_as_dict = players_as_dictionaries(squads_list)
    
    dict_of_positions = {}
    
    for player in players_as_dict:
        
        dict_of_positions.setdefault(player['position'], [])
        
        dict_of_positions[player['position']].append(player)
        
    
    return dict_of_positions

