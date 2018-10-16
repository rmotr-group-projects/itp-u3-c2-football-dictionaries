from .squads_data import SQUADS_DATA
from pprint import pprint

def players_as_dictionaries(squads_list):
    player_list = []
    for squad in squads_list:
        player = {}
        player['caps'] = squad[4]
        player['club'] = squad[5]
        player['club_country'] = squad[7]
        player['country'] = squad[6]
        player['date_of_birth'] = squad[3]
        player['name'] = squad[2]
        player['number'] = squad[0]
        player['position'] = squad[1]
        player['year'] = squad[8]
        player_list.append(player)
    return player_list

# print(players_as_dictionaries(SQUADS_DATA))

squads_list = players_as_dictionaries(SQUADS_DATA)
# pprint(squads_list[0])
# print(len(squads_list))

# {
#         'caps': '',
#         'club': 'Quilmes',
#         'club_country': 'Argentina',
#         'country': 'Argentina',
#         'date_of_birth': '(1908-10-23)23 October 1908 (aged 21)',
#         'name': 'Juan Botasso',
#         'number': '1',
#         'position': 'GK',
#         'year': '1930'
#     }
