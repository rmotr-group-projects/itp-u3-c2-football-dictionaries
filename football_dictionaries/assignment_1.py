def players_as_dictionaries(squads_list):
    resultlist = []
    for squad in squads_list:
        playerdict = {
        'caps': squad[4],
        'club': squad[5],
        'club_country': squad[7],
        'country': squad[6],
        'date_of_birth': squad[3],
        'name': squad[2],
        'number': squad[0],
        'position': squad[1],
        'year': squad[8]
        }
        resultlist.append(playerdict)
    return resultlist
    
   