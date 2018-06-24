# # Please note we're returning a dictionary instead of a list
# {
#   "GK": [{..player1..}, {..player2..}],
#   "DF": [{..player1..}, {..player2..}],
#   "MF": [{..player1..}, {..player2..}],
#   "FW": [{..player1..}, {..player2..}],
# }
from squads_data import SQUADS_DATA
def players_by_position(squads_list):
    result = {
        'GK' : [],
        'DF' : [],
        'MF' : [],
        'FW' : []
    }
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
        if temp_obj['position'] == 'GK':
            result['GK'].append(temp_obj)
        elif temp_obj['position'] == 'DF':
            result['DF'].append(temp_obj)
        elif temp_obj['position'] == 'MF':
            result['MF'].append(temp_obj)
        else:
            result['FW'].append(temp_obj)
    return result
print(players_by_position(SQUADS_DATA))
