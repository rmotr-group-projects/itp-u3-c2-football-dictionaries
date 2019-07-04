def players_by_position(squads_list):
    pos_dict = {}
    for player in squads_list:
        pos_dict.setdefault(player[1], [])
        player_dict = {}
        player_dict['number'] = player[0]
        player_dict['position'] = player[1]
        player_dict['name'] = player[2]
        player_dict['date_of_birth'] = player[3]
        player_dict['caps'] = player[4]
        player_dict['club'] = player[5]
        player_dict['country'] = player[6]
        player_dict['club_country'] = player[7]
        player_dict['year'] = player[8]
        pos_dict[player[1]].append(player_dict)
    return pos_dict
