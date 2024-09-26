from .assignment_1 import players_as_dictionaries
from .squads_data import SQUADS_DATA
from pprint import pprint

def players_by_position(squads_list):
    ''' Group players information into dictionaries by position. '''
    positions = {}
    team = players_as_dictionaries(squads_list)
    
    for player in team:
        position = player['position']
        positions.setdefault(position, [])
        positions[position].append(player)
        # pprint(positions)
    return positions

pprint(players_by_position(SQUADS_DATA))


'''
# Please note we're returning a dictionary instead of a list
{
  "GK": [{..player1..}, {..player2..}],
  "DF": [{..player1..}, {..player2..}],
  "MF": [{..player1..}, {..player2..}],
  "FW": [{..player1..}, {..player2..}],
}
'''
        
