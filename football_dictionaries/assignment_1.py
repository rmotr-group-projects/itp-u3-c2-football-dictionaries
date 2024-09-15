def players_as_dictionaries(squads_list):
    players = {
        'number': '',
        'position': '',
        'name': '',
        'date_of_birth': '',
        'caps': '',
        'club': '',
        'country': '',
        'club_country': '',
        'year': ''
    }
    player_list = []
    
    for player in squads_list:
        players['number']       = player[0]
        players['position']     = player[1]
        players['name']         = player[2]
        players['date_of_birth'] = player[3]
        players['caps']         = player[4]
        players['club']         = player[5]
        players['country']      = player[6]
        players['club_country'] = player[7]
        players['year']         = player[8]
        
        player_list.append(players.copy())
    
    return player_list

