def players_by_position(sqauds_data):
    player_dict_list = []
    playerlist=[]
    count = 0 
    goalkeepers = []
    midfielders = []
    forwards = []
    for players in sqauds_data:
        playerlist += [players]
        player_dict_list=[{
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
        if playerlist[count][1] == 'GK':
            goalkeepers+=(player_dict_list)
   
        elif playerlist[count][1] == "MF":
            midfielders+=(player_dict_list)
        else:
            forwards+=(player_dict_list)
        count+=1
    players_pos_dic ={
        'GK': goalkeepers,
        'MF': midfielders,
        'FW': forwards
        }
    return(players_pos_dic)
