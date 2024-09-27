from pprint import pprint
from football_dictionaries.assignment_1 import players_as_dictionaries
#from squads_data import SQUADS_DATA

def players_by_country_and_position(squads_list):
    squads = players_as_dictionaries(squads_list) # [{},{},{}]
    squad_dict = {}
    for squad in squads:
        country = squad['country']
        pos = squad ['position']
        squad_dict.setdefault(country,{})
        squad_dict[country].setdefault(pos,[])
        squad_dict[country][pos].append(squad)
    return squad_dict
    #pprint (squad_dict.keys())

#players_by_country_and_position(SQUADS_DATA)
"""
{
  "Argentina": {
    "GK": [{..player1..}, {..player2..}],
    "DF": [{..player1..}, {..player2..}],
    "MF": [{..player1..}, {..player2..}],
    "FW": [{..player1..}, {..player2..}],
  },
  "Brazil": {
    "GK": [{..player1..}, {..player2..}],
    "DF": [{..player1..}, {..player2..}],
    "MF": [{..player1..}, {..player2..}],
    "FW": [{..player1..}, {..player2..}],
  }
}


"""