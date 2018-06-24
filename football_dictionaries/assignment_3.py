from squads_data import SQUADS_DATA
from pprint import pprint
def players_by_country_and_position(squads_data):
    player_dict_list = []
    playerlist=[]
    count = 0
    count2 = 0
    agoalkeepers = []
    amidfielders = []
    aforwards = []
    bzgoalkeepers = []
    bzmidfielders = []
    bzforwards = []
    belgoalkeepers = []
    belmidfielders = []
    belforwards = []
    skgoalkeepers = []
    skmidfielders = []
    skforwards = []
    argentina = []
    brazil = []
    belgium = []
    south_korea=[]
    for players in squads_data:
        playerlist += [players]
        player_dict_list==[{
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
        if playerlist[count][6] == 'Argentina':
            argentina+= playerlist[count]
            if playerlist[count][1]=='GK':
                agoalkeepers+=playerlist[count]
            elif playerlist[count][1]=='MF':
                amidfielders+=playerlist[count]
            else:
                aforwards+=playerlist[count]
        elif playerlist[count][6] == 'Brazil':
            brazil+=playerlist[count]
            if playerlist[count][1]=='GK':
                bzgoalkeepers+=playerlist[count]
            if playerlist[count][1]=='MF':
                bzmidfielders+=playerlist[count]
            else:
                bzforwards+=playerlist[count]
        elif playerlist[count][6] == 'Belgium':
            belgium+= playerlist[count]
            if playerlist[count][1]=='GK':
                belgoalkeepers+=playerlist[count]
            elif playerlist[count][1]=='MF':
                belmidfielders+=playerlist[count]
            else:
                belforwards+=playerlist[count]
        else:
            south_korea+= playerlist[count]
            if playerlist[count][1]=='GK':
                skgoalkeepers+=playerlist[count]
            elif playerlist[count][1]=='MF':
                skmidfielders+=playerlist[count]
            else:
                skforwards+=playerlist[count]

        count+=1
    
  
        big_dic={
        'Argentina': {
            'GK': agoalkeepers,
            
            'FW': aforwards
        },
        'Brazil': {
             'GK': bzgoalkeepers,
             'MF': bzmidfielders,
             'FW': bzforwards   
        },
        'Belgium': {
             'GK': belgoalkeepers,
             'MF': belmidfielders,
             'FW': belforwards   
        },
        'South Korea': {
             'GK': skgoalkeepers,
             'MF': skmidfielders,
             'FW': skforwards  
            }
        }
    return(big_dic)
        
pprint(players_by_country_and_position(SQUADS_DATA))
