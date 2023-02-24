def players_as_dictionaries(squads_list):
    final_list = []
    for item in squads_list:
        final_dict = {'number': item[0],
        'position': item[1],
        'name': item[2],
        'date_of_birth': item[3],
        'caps': item[4],
        'club': item[5],
        'country': item[6],
        'club_country': item[7],
        'year': item[8]}
        final_list.append(final_dict)
    return final_list