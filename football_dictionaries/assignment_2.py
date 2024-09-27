def players_by_position(squads_list):
    positions = {}
    for player in squads_list:
        positions.setdefault(player[1], []) 
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
        positions[player[1]].append(player_dict)
    return positions
