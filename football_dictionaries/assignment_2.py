def players_by_position(squads_list):
    squad_dict = {}
    
    for player in squads_list:
        position = player[1]
        squad_dict.setdefault(position, [])
        player_dict = {
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
        squad_dict[position].append(player_dict)
        
        
    return squad_dict 
        
