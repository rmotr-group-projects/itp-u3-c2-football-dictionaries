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
from assignment_1 import players_as_dictionaries
from squads_data import SQUADS_DATA
from pprint import pprint 
def players_by_country_and_position(squads_list):
    result = {}
    pprint(squads_list)
    for player in squads_list:
        result.setdefault(player['country'], {})
        result[player['country']].setdefault(player['position'], [])
        result[player['country']][player['position']].append(player)
    pprint(result)
    return result
players_by_country_and_position(players_as_dictionaries(SQUADS_DATA))
        
