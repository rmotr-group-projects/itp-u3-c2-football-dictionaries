def player_to_dict(player):
    player_as_dict = {
        'number': player[0],
        'position': player[1],
        'name': player[2],
        'date_of_birth': player[3],
        'caps': player[4],
        'club': player[5],
        'country': player[6],
        'club_country': player[7],
        'year': player[8]
    }
    
    return player_as_dict

def players_by_position(squads_list):
    position_dict = {}
    
    for player in squads_list:
        player_dict = player_to_dict(player)
        position = player_dict['position']
        position_dict.setdefault(position, [])
        position_dict[position].append(player_dict)
    
    return position_dict

