def players_by_country_and_position(squads_list):
    country_dict = {}
    for player in squads_list:
        pos_dict = {}
        player_dict = {}
        country_dict.setdefault(player[6], {})
        country_dict[player[6]].setdefault(player[1], [])
        player_dict['number'] = player[0]
        player_dict['position'] = player[1]
        player_dict['name'] = player[2]
        player_dict['date_of_birth'] = player[3]
        player_dict['caps'] = player[4]
        player_dict['club'] = player[5]
        player_dict['country'] = player[6]
        player_dict['club_country'] = player[7]
        player_dict['year'] = player[8]
        country_dict[player[6]][player[1]].append(player_dict)
    return country_dict