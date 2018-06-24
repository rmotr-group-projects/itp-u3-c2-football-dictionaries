# {
#   "Argentina": {
#     "GK": [{..player1..}, {..player2..}],
#     "DF": [{..player1..}, {..player2..}],
#     "MF": [{..player1..}, {..player2..}],
#     "FW": [{..player1..}, {..player2..}],
#   },
#   "Brazil": {
#     "GK": [{..player1..}, {..player2..}],
#     "DF": [{..player1..}, {..player2..}],
#     "MF": [{..player1..}, {..player2..}],
#     "FW": [{..player1..}, {..player2..}],
#   }
# }
from squads_data import SQUADS_DATA
from pprint import pprint 
def players_by_country_and_position(squads_list):
    result = {}
    for player in squads_list:
        temp_obj = {
            'number'        : player[0],
            'position'      : player[1],
            'name'          : player[2],
            'date_of_birth' : player[3],
            'caps'          : player[4],
            'club'          : player[-4],
            'country'       : player[-3],
            'club_country'  : player[-2],
            'year'          : player[-1]
        }
        key_check = temp_obj['country']
        position_check = temp_obj['position']
        if key_check in result:
            if position_check in result[key_check]:
                result[key_check][position_check].append(temp_obj)
            else:
                result[key_check][position_check] = []
                result[key_check][position_check].append(temp_obj) 
        else:
            result[key_check] = {}
            result[key_check][temp_obj['position']] = []
            result[key_check][temp_obj['position']].append(temp_obj)
    return result
pprint(players_by_country_and_position(SQUADS_DATA))
        
