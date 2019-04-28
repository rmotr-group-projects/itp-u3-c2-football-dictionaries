from assignment_1 import players_as_dictionaries
from assignment_2 import players_by_position
from .squads_data import SQUADS_DATA
from pprint import pprint

def players_by_country_and_position(squads_list):
    '''Group players by country, and per each country, group players by position.'''
    country_dict = {}
    team = players_as_dictionaries(squads_list)
    for player in team:
        position = player['position']
        country = player['country']
        country_dict.setdefault(country, {})
        country_dict[country].setdefault(position, [])
        country_dict[country][position].append(player)
        # pprint(country_dict)
    return country_dict

pprint(players_by_country_and_position(SQUADS_DATA))

'''
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
  },
  "Brazil": {
    "GK": [{..player1..}, {..player2..}],
    "DF": [{..player1..}, {..player2..}],
    "MF": [{..player1..}, {..player2..}],
    "FW": [{..player1..}, {..player2..}],
  }
  "South Korea": {
    "GK": [{..player1..}, {..player2..}],
    "DF": [{..player1..}, {..player2..}],
    "MF": [{..player1..}, {..player2..}],
    "FW": [{..player1..}, {..player2..}],
  }
}
'''