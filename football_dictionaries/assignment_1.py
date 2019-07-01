def players_as_dictionaries(squads_list):
    squads_dict_list = []
    for squad in squads_list:
        squads_dict_list.append({
                'number': squad[0],
                'position': squad[1],
                'name': squad[2],
                'date_of_birth': squad[3],
                'caps': squad[4],
                'club': squad[5],
                'country': squad[6],
                'club_country': squad[7],
                'year': squad[8],
            })
    return squads_dict_list