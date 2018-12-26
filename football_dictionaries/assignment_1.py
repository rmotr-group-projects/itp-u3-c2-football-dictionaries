def players_as_dictionaries(squads_list):
    result = []
    for each in squads_list:
        player = {
            'number': each[0],
            'position': each[1],
            'name': each[2],
            'date_of_birth': each[3],
            'caps': each[4],
            'club': each[5],
            'country': each[6],
            'club_country': each[7],
            'year': each[8],
        }
        result.append(player)
    return result