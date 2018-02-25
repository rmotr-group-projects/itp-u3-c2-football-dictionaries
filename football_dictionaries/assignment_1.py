def players_as_dictionaries(squads_list):
    
    result = [] 
    
    for player in squads_list:
        player_dict = {}
        player_dict['number'] = player[0]
        player_dict['position'] = player[1]
        player_dict['name'] = player[2]
        player_dict['date_of_birth'] = player[3]
        player_dict['caps'] = player[4]
        player_dict['club'] = player[-4]
        player_dict['country'] = player[-3]
        player_dict['club_country'] = player[-2]
        player_dict['year'] = player[-1]
        result.append(player_dict)
    
    return result