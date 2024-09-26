from football_dictionaries.squads_data import SQUADS_DATA
from pprint import pprint


def players_as_dictionaries(squads_list):
    final_list = []
    for player in squads_list:
        player_dict = {}
        player_dict['number'] = player[0]
        player_dict['position'] = player[1]
        player_dict['name'] = player[2]
        player_dict['date_of_birth'] = player[3]
        player_dict['caps'] = player[4]
        player_dict['club'] = player[5]
        player_dict['country'] = player[6]
        player_dict['club_country'] = player[7]
        player_dict['year'] = player[8]
        final_list.append(player_dict)
    return final_list

'''
i = 0
for s in SQUADS_DATA:
    l = len(s)
    j = 0
    while j < l:
        pprint(s[j])
        j += 1
    i += 1
    if i > 0:
        break
'''
pprint(players_as_dictionaries(SQUADS_DATA))