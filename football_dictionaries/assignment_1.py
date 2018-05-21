def players_as_dictionaries(squads_list):
    squad = []

    for p in squads_list:
        player = {
            'number': p[0],
            'position': p[1],
            'name': p[2],
            'date_of_birth': p[3],
            'caps': p[4],
            'club': p[5],
            'country': p[6],
            'club_country': p[7],
            'year': p[8]
        }

        squad.append(player)

    return squad