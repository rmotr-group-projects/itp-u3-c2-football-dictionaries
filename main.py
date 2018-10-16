"""
from football_dictionaries.squads_data import SQUADS_DATA
from football_dictionaries.assignment_1 import players_as_dictionaries
from pprint import pprint


  
result = players_as_dictionaries(SQUADS_DATA)
pprint(result)
"""

player_as_list = [
    "1",
    "GK",
    "Juan Botasso",
    "(1908-10-23)23 October 1908 (aged 21)",
    "",
    "Quilmes",
    "Argentina",
    "Argentina",
    "1930"
  ]
  
player_as_dict = {
        'caps': player_as_list[4],
        'club': player_as_list[5],
        'club_country': player_as_list[7],
        'country': player_as_list[6],
        'date_of_birth': player_as_list[3],
        'name': player_as_list[2],
        'number': player_as_list[0],
        'position': player_as_list[1],
        'year': player_as_list[8]
    }

assert player_as_dict == {
        'caps': '',
        'club': 'Quilmes',
        'club_country': 'Argentina',
        'country': 'Argentina',
        'date_of_birth': '(1908-10-23)23 October 1908 (aged 21)',
        'name': 'Juan Botasso',
        'number': '1',
        'position': 'GK',
        'year': '1930'
    }
print(player_as_dict)