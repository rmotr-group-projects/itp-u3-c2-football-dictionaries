def players_by_country_and_position(squads_data):
    player_dict_list = []
    playerlist=[]
    count = 0
    brazil = []
    belgium = []
    south_korea=[]
    a_gk = []
    a_mf = []
    a_fwd = []
    sk_gk = []
    sk_mf = []
    sk_fwd = []
    br_gk = []
    br_mf = []
    br_fwd = []
    bel_gk = []
    bel_mf = []
    bel_fwd = []
    for players in squads_data:
        playerlist += [players]
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
        
    
        for players in [player_dict_list]:
            if (players[count]).get('country') is 'Argentina':
                if (players[count].get('position')):
                    a_gk.append(players[count])
                elif (players[count]).get('position')=='MF':
                    a_mf.append(players[count])
                else:
                    a_fwd.append(players[count])
            if (players[count]).get('country') is 'Brazil':
                if (players[count].get('position')) is 'GK':
                    br_gk.append(players[count])
                elif (players[count]).get('position') is 'MF':
                    br_mf.append(players[count])
                else:
                    br_fwd.append(players[count])
            if (players[count]).get('country') == 'Belgium':
                if (players[count].get('position')) is 'GK':
                    bel_gk.append(players[count])
                elif (players[count]).get('position') is 'MF':
                    bel_mf.append(players[count])
                else:
                    bel_fwd.append(players[count])
            if (players[count]).get('country') == 'South Korea':
                if (players[count].get('position')) is 'GK':
                    sk_gk.append(players[count])
                elif (players[count]).get('position') is 'MF':
                    sk_mf.append(players[count])
                else:
                    sk_fwd.append(players[count])
        count+=1
    big_dic={
        'Argentina':{
            'GK': [a_gk],
            #'MF': a_mf,
            'FW': [a_fwd]
            },
        'Brazil':{
            #'GK': br_gk,
            'MF': br_mf,
            #'FW': br_fwd
            },
        'Belgium':{
            'GK': bel_gk,
            'MF': bel_mf,
            'FW': bel_fwd
            },
        'South Korea':{
            'GK': sk_gk,
            'MF': sk_mf,
            'FW': sk_fwd
        }
    }

    return(big_dic)