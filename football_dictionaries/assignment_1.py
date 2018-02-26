def players_as_dictionaries(squads_list):
    info_list = ['number', 'position', 'name', 'date_of_birth', 'caps', 'club', 'country', 'club_country', 'year']
    
    player_list = []
    
    for player in squads_list:
        new_player_dict = {}
        for i, attribute in enumerate(player):
            new_player_dict[info_list[i]] = attribute
        player_list.append(new_player_dict)
    return player_list
