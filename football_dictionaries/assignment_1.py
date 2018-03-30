def players_as_dictionaries(squads_list):
    result=[]
    for list in squads_list:
        player={
        'number':list[0],
        'position':list[1],
        'name':list[2],
        'date_of_birth':list[3],
        'caps':list[4],
        'club':list[5],
        'country':list[6],
        'club_country':list[7],
        'year':list[8],
        }
        result.append(player)
    return result