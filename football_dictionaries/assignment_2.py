from .assignment_1 import players_as_dictionaries
from .squads_data import SQUADS_DATA

'''# Please note we're returning a dictionary instead of a list
{
  "GK": [{..player1..}, {..player2..}],
  "DF": [{..player1..}, {..player2..}],
  "MF": [{..player1..}, {..player2..}],
  "FW": [{..player1..}, {..player2..}],
}
'''
'''
def players_as_dictionaries(squads_list):
    player_list = [
    'number',
    'position',
    'name',
    'date_of_birth',
    'caps',
    'club',
    'club_country',
    'country',
    'year']
    final_list = []
    for player in squads_list:
        final_list.append(dict(zip(player_list, player)))
    return final_list
'''

def players_by_position(squads_list):
    final_dictionary = {}
    players = players_as_dictionaries(squads_list)
    
    for player in players:
        key = player['position']
        final_dictionary.setdefault(key, [])
        final_dictionary[key].append(player)
        
        
    return final_dictionary
        
print(players_by_position(SQUADS_DATA))