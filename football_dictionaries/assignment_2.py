def players_by_position(squads_list):
    players_as_dicts = {}
    for player in squads_list:
        #if players_as_dicts:
        if player[1] not in players_as_dicts:
            players_as_dicts[player[1]] = [
                {
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
            ]
        else:
            players_as_dicts[player[1]].append(
                {
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
            )
    return players_as_dicts

