def player_list_to_dict(player_list):
    dict_keys = [
        'number', 
        'position', 
        'name', 
        'date_of_birth',  
        'caps',
        'club',
        'country',
        'club_country',
        'year'
        ]
    
    player_dict = {}
    
    for index, elem in enumerate(dict_keys):
        player_dict[elem] = player_list[index]
    
    return player_dict
    


def players_as_dictionaries(squads_list):
    result = []
    
    for player_as_list in squads_list:
        player_as_dict = player_list_to_dict(player_as_list)
        result.append(player_as_dict)
    
    return result