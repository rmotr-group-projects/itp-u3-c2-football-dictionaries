def players_as_dictionaries(squads_list):
    a_list = []
    for player in squads_list:
        p_dict = {
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
        a_list.append(p_dict)
    return a_list