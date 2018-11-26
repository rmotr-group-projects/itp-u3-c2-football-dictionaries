def players_by_position(squads_list):
    a_list = []
    for player in squads_list:
        a_list.append({
            'number': player[0],
            'position': player[1],
            'name': player[2],
            'date_of_birth': player[3],
            'caps': player[4],
            'club': player[5],
            'country': player[6],
            'club_country': player[7],
            'year': player[8],
        })
    
    a_dict = {}
    for person in a_list:
        position = person['position']
        a_dict.setdefault(position, [])
        a_dict[position].append(person)
    
    return a_dict