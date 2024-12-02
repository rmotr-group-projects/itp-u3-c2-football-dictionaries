def players_as_dictionaries(SQUADS_DATA):
    
    players = []
    for player in SQUADS_DATA:
        play_dict = {
            'number': player[0],
            'position': player[1] ,
            'name': player[2],
            'date_of_birth': player[3],
            'caps': player[4],
            'club': player[5],
            'country': player[6],
            'club_country':player[7],
            'year': player[8],
            }

        players.append(play_dict)
    return players