def players_by_position(squads_list):
    position_dict = {
        'GK': [],
        'MF': [],
        'FW': []
    }
    
    for player in squads_list:
        entry = {
            'caps': player[4],
            'club': player[5],
            'club_country': player[6],
            'country': player[7],
            'date_of_birth': player[3],
            'name': player[2],
            'number': player[0],
            'position': player[1],
            'year': player[8]
        }
        
        position = entry['position']
        position_dict[position].append(entry)
   
    
    return position_dict