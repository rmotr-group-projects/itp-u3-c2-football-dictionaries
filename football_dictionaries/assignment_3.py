from .assignment_1 import players_as_dictionaries
from .assignment_2 import players_by_position
from .squads_data import SQUADS_DATA

def players_by_country_and_position(squads_list):
    # create a dictionary by country
    profiles = players_as_dictionaries(squads_list) # list of dictionaries
    # positions = players_by_position(squads_list) # dictionary by positions
    countries = {}
    positions = {}

    # create a dictionary by countries
    for player in profiles:
        countries.setdefault(player['country'], {})
        countries[player['country']].setdefault(player['position'], []).append(player)
    return countries

# print(players_by_country_and_position(SQUADS_DATA))
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