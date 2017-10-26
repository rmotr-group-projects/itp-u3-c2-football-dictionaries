def players_as_dictionaries(squads_list):
    dict_of_players = []
    for players in squads_list:
        players_in_dict = {
            'number' : players[0],
            'position' : players[1],
            'name' : players[2],
            'date_of_birth' : players[3],
            'caps' : players[4],
            'club' : players[5],
            'club_country' : players[7],
            'country' : players[6],
            'year' : players[8]
        }
        dict_of_players.append(players_in_dict)
    return dict_of_players
