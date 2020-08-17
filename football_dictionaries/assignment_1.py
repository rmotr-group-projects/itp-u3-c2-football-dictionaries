def players_as_dictionaries(squads_list):
    player_list=[]
    for squad in squads_list:
        player={
            'caps': squad[4],
            'club': squad[5],
            'club_country': squad[7],
            'country':  squad[6],
            'date_of_birth':  squad[3],
            'name':  squad[2],
            'number':  squad[0],
            'position':  squad[1],
            'year':  squad[-1]
        }
        player_list.append(player)
    return player_list