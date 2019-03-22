def players_as_dictionaries(squads_list):
    SQUADS_DATA={}
    
    SQUADS_DATA['number']=squads_list[0],
    SQUADS_DATA['position']=squads_list[1],
    SQUADS_DATA['name']=squads_list[2],
    SQUADS_DATA['date_of_birth']=squads_list[3],
    SQUADS_DATA['caps']=squads_list[4],
    SQUADS_DATA['club']=squads_list[5],
    SQUADS_DATA['country']=squads_list[6],
    SQUADS_DATA['club_country']=squads_list[7],
    SQUADS_DATA['year']=squads_list[8]
    return SQUADS_DATA
    