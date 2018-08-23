def players_as_dictionaries(SQUADS_DATA):
    full_list=[]
    for i in SQUADS_DATA:
        full_list.append({
            'number': i[0],
            'position':i[1],
            'name':i[2],
            'date_of_birth':i[3],
            'caps':i[4],
            'club':i[5],
            'country':i[6],
            'club_country':i[7],
            'year':i[8]
        })

    SQUADS_DATA=full_list
    return SQUADS_DATA