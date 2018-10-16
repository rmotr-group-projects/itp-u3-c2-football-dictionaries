def players_as_dictionaries(squads_list):
    result = []
    for player in squads_list:
        result.append({
            'number'        : player[0],
            'position'      : player[1],
            'name'          : player[2],
            'date_of_birth' : player[3],
            'caps'          : player[4],
            'club'          : player[-4],
            'country'       : player[-3],
            'club_country'  : player[-2],
            'year'          : player[-1]
        })
    return result