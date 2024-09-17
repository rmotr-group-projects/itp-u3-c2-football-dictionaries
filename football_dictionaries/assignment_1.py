def players_as_dictionaries(squads_list):
    result = []
    
    for player in squads_list:
        player_dict = {
            'caps': player[4],
            'club': player[5],
            'country': player[6],
            'club_country': player[7],
            'date_of_birth': player[3],
            'name': player[2],
            'number': player[0],
            'position': player[1],
            'year': player[8]   
        }
        result.append(player_dict)

    return result

    