def players_as_dictionaries(squads_list):
    players = []
    for squad in squads_list:
        new_list = {
        'caps': squad[4],
        'club': squad[5],
        'club_country': squad[6],
        'country': squad[7],
        'date_of_birth': squad[3],
        'name': squad[2],
        'number': squad[0],
        'position': squad[1],
        'year': squad[8]
        }
        players.append(new_list)
    return players

