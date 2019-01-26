def players_by_country_and_position(squads_list):
    cnt_pos_dict = {}
    for player in squads_list:
        country = player[-3]
        position = player[1]
        cnt_pos_dict.setdefault(country,{})
        cnt_pos_dict[country].setdefault(position, [])
        cnt_pos_dict[country][position].append({
            'number':player[0],
            'position':player[1],
            'name':player[2],
            'date_of_birth':player[3],
            'caps':player[4],
            'club':player[5],
            'country':player[6],
            'club_country':player[7],
            'year':player[8]
        })
    return cnt_pos_dict