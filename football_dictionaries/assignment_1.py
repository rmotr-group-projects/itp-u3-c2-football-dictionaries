def players_as_dictionaries(sqauds_data):
    player_dict_list = []
    playerlist = []
    newlist = []
    count = 0 
    for playerinfo in sqauds_data:
        playerlist+=[playerinfo]
        player_dict_list+=[{
            'number': playerlist[count][0],
            'position': playerlist[count][1],
            'name': playerlist[count][2],
            'date_of_birth': playerlist[count][3],
            'caps': playerlist[count][4],
            'club': playerlist[count][5],
            'country': playerlist[count][6],
            'club_country': playerlist[count][7],
            'year': playerlist[count][8],
             }]
        count+=1
    return(player_dict_list)
