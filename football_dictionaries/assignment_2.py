#from squads_data import SQUADS_DATA
from football_dictionaries.assignment_1 import players_as_dictionaries
from pprint import pprint


def players_by_position(squads_list):
    squad_dict = {}
    squads = players_as_dictionaries (squads_list)
    for squad in squads: #every squad is a dict
        pos = squad['position']
        squad_dict.setdefault(pos,[])
        squad_dict[pos].append(squad)
        
    return squad_dict
    
    # result = [{'GK': squad},{'MF':, ....]
    
    
#players_by_position(SQUADS_DATA)

"""
{
  "GK": [{..player1..}, {..player2..}],
  "DF": [{..player1..}, {..player2..}],
  "MF": [{..player1..}, {..player2..}],
  "FW": [{..player1..}, {..player2..}],
}

"""