"""
# code from
#https://stackoverflow.com/questions/31071888/python-group-list-items-in-a-dict

#Working / tested and passed.
"""


def players_by_position(squads_list):
    groupby_dict = {}
    new_squads_data = [
        {'number': x[0], 'position': x[1], 'name': x[2], 'date_of_birth': x[3], 'caps': x[4], 'club': x[5],
         'country': x[6], 'club_country': x[7], 'year': x[8], } for x in squads_list]
    print(new_squads_data)
    for e in new_squads_data:
        groupby_dict[e['position']] = groupby_dict.get(e['position'], [])
        groupby_dict[e['position']].append(e)
    return groupby_dict



"""
Santiago's solution on Youtube trying out

from football_dictionaries.squads_data import SQUADS_DATA
squads_list = SQUADS_DATA

def transform_list_player_to_dict(player_as_list):
    player_as_dict = {
        'number': player_as_list[0],
        'position': player_as_list[1],
        'name': player_as_list[2],
        'date_of_birth': player_as_list[3],
        'caps': player_as_list[4],
        'club': player_as_list[5],
        'country': player_as_list[6],
        'club_country': player_as_list[7],
        'year': player_as_list[8],
    }
    return player_as_dict


def players_as_dictionaries(squads_list):
    players_list = []
    for player in squads_list:
        player_as_dict = transform_list_player_to_dict(player)
        players_list.append(player_as_dict)
    print(players_list)
    return players_list

def players_by_position(squads_list):
    players = {}

    for player_as_list in squads_list:
        player = transform_list_player_to_dict(player_as_list)
        position = player['position']

        if position not in players:
            players['position'] = []

        list_by_position = players.get(position)
        list_by_position.append(player)

    return players






from football_dictionaries.squads_data import SQUADS_DATA
squads_list = SQUADS_DATA
testcode = players_as_dictionaries(squads_list)
print(testcode)

# Test function locally
from football_dictionaries.squads_data import SQUADS_DATA
squads_list = SQUADS_DATA
testcode = players_by_position(squads_list)
print(testcode)
"""


