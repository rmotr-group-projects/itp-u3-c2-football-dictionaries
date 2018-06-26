# # Please note we're returning a dictionary instead of a list
# {
#   "GK": [{..player1..}, {..player2..}],
#   "DF": [{..player1..}, {..player2..}],
#   "MF": [{..player1..}, {..player2..}],
#   "FW": [{..player1..}, {..player2..}],
# }
from assignment_1 import players_as_dictionaries
from squads_data import SQUADS_DATA
import pprint
def players_by_position(squads_list):
    result_dict = {}
    for player in squads_list:
        result_dict.setdefault(player['position'], [])
        result_dict[player['position']].append(player)
    pprint.pprint(result_dict)
    return result_dict
        
players_by_position(players_as_dictionaries(SQUADS_DATA))
