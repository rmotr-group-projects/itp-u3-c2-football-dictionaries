def players_by_position(squads_list):
    position_dict = {}
    for player in squads_list:
        position = player[1]
        position_dict.setdefault(position, [])
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
        position_dict[position].append(player_dict)
    return position_dict
        