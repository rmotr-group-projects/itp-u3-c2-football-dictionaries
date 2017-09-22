def players_as_dictionaries(squads_list):
    player_list = []
    player_key = ('number', 'position', 'name', 'date_of_birth', 'caps', 'club', 'country', 'club_country', 'year')
    
    for player in squads_list:
        player_list.append(dict(zip(player_key, player)))
    
    return player_list