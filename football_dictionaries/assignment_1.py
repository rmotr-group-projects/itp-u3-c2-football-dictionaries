def players_as_dictionaries(squads_list):
    player_list = []
    
    for player in squads_list:
        # append dictionaries to the player_list
        current_player = {}
        current_player.setdefault('number', player[0])
        current_player.setdefault('position', player[1])
        current_player.setdefault('name', player[2])
        current_player.setdefault('date_of_birth', player[3])
        current_player.setdefault('caps', player[4])
        current_player.setdefault('club', player[5])
        current_player.setdefault('country', player[6])
        current_player.setdefault('club_country', player[7])
        current_player.setdefault('year', player[8])
        player_list.append(current_player)
    
    return player_list