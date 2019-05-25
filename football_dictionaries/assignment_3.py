    
def players_by_country_and_position(squads_list):
    players_dict = {}
    for player in  squads_list:
        if player[6] not in players_dict:
            players_dict[player[6]] = {}

        if player[1] not in players_dict[player[6]]:
            players_dict[player[6]][player[1]] = [
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
            players_dict[player[6]][player[1]].append(
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

    return players_dict

        