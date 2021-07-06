def players_by_position(squads_list):
    master_list = []
    
    for player in squads_list:
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
        
        master_list.append(player_dict)
    
    
    positions_list = {}
    
    for player in master_list:
        position = player['position']
        if position not in positions_list:
            positions_list.setdefault(position, [])
        positions_list[position].append(player)
    
    return positions_list