from squads_data import SQUADS_DATA
from pprint import pprint
def players_by_country_and_position(squads_data):
    player_dict_list = []
    playerlist=[]
    count = 0
    goalkeepers = []
    midfielders = []
    forwards = []
    argentina = []
    brazil = []
    belgium = []
    south_korea=[]
    for players in squads_data:
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
        
        if playerlist[count][6] == 'Argentina':
            if playerlist[count][1] == 'GK':
                goalkeepers+=(player_dict_list)
            elif playerlist[count][1] == "MF":
                midfielders+=(player_dict_list)
            else:
                forwards+=(player_dict_list)
        if playerlist[count][6] == 'Brazil':
            if playerlist[count][1] == 'GK':
                goalkeepers+=(player_dict_list)
            elif playerlist[count][1] == "MF":
                midfielders+=(player_dict_list)
            else:
                forwards+=(player_dict_list)
        if playerlist[count][6] == 'Belgium':
            if playerlist[count][1] == 'GK':
                goalkeepers+=(player_dict_list)
            elif playerlist[count][1] == "MF":
                midfielders+=(player_dict_list)
            else:
                forwards+=(player_dict_list)
        if playerlist[count][6] == 'South Korea':
            if playerlist[count][1] == 'GK':
                goalkeepers+=(player_dict_list)
            elif playerlist[count][1] == "MF":
                midfielders+=(player_dict_list)
            else:
                forwards+=(player_dict_list)
        count+=1
    big_dic={
        'Argentina': {
            'GK': goalkeepers,
            'MF': midfielders,
            'FW': forwards
        },
         
         
        'Brazil': {
             'GK': goalkeepers,
             'MF': midfielders,
             'FW': forwards   
        },
        'Belgium': {
             'GK': goalkeepers,
             'MF': midfielders,
             'FW': forwards   
        },
        'South Korea': {
             'GK': goalkeepers,
             'MF': midfielders,
             'FW': forwards  
            }
        }
    return(big_dic) 