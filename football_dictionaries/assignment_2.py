def players_by_position(squads_list):
    positions = {"GK": [], "MF" : [], "FW" : []}
    for squad in squads_list:
        if 'GK' in squad:
            positions['GK'].append({
                'caps': squad[4],
                'club': squad[5],
                'club_country': squad[6],
                'country': squad[7],
                'date_of_birth': squad[3],
                'name': squad[2],
                'number': squad[0],
                'position': squad[1],
                'year': squad[8]
            })
        elif 'MF' in squad:
             positions['MF'].append({
                'caps': squad[4],
                'club': squad[5],
                'club_country': squad[6],
                'country': squad[7],
                'date_of_birth': squad[3],
                'name': squad[2],
                'number': squad[0],
                'position': squad[1],
                'year': squad[8]
            })
        elif 'FW' in squad: 
              positions['FW'].append({
                'caps': squad[4],
                'club': squad[5],
                'club_country': squad[6],
                'country': squad[7],
                'date_of_birth': squad[3],
                'name': squad[2],
                'number': squad[0],
                'position': squad[1],
                'year': squad[8]
            })
    return positions