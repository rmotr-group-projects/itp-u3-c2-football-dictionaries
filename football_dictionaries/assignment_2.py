def players_by_position(squads_list):
    position_dictionary = {}
    for player in squads_list:
        position = player[1]
        position_dictionary.setdefault(position,[])
        position_dictionary[position].append({
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
    return(position_dictionary)

