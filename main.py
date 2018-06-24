from football_dictionaries.squads_data import SQUADS_DATA
from football_dictionaries.assignment_1 import players_as_dictionaries
from pprint import pprint

def players_as_dictionaries(SQUADS_DATA):
    player_dict_list = []
    playerlist = []
    newlist = []
    count = 0
    for playerinfo in SQUADS_DATA:
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
#pprint(players_as_dictionaries(SQUADS_DATA))

def players_by_position(SQUADS_DATA):
    player_dict_list = []
    playerlist=[]
    count = 0
    goalkeepers = []
    defenders = []
    midfielders = []
    forwards = []
    for players in SQUADS_DATA:
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
        'DF': defenders,
        'MF': midfielders,
        'FW': forwards
        }
    return(players_pos_dic)
    
result = (players_by_position(SQUADS_DATA))

print(len(result))