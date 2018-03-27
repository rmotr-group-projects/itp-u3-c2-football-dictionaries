# from squads_data import SQUADS_DATA
from football_dictionaries.squads_data import SQUADS_DATA
from pprint import pprint

def players_as_dictionaries(squads_list):
    # squads_player_dict = {
    #     'number': None,
    #     'position': None,
    #     'players_name': None,
    #     'date_of_birth': None,
    #     'caps': None,
    #     'club': None,
    #     'country': None,
    #     'club_country': None,
    #     'year': None
    # }
    # # single_player = []
    players_list = []
    index = 0
    for player in squads_list:
        squads_player_dict = {}
        # single_player['number'] = player[0]
        # squads_player_dict.update(single_player)
        squads_player_dict['number'] = player[0]
        squads_player_dict['position'] = player[1]
        squads_player_dict['name'] = player[2]
        squads_player_dict['date_of_birth'] = player[3]
        squads_player_dict['caps'] = player[4]
        squads_player_dict['club'] = player[5]
        squads_player_dict['country'] = player[6]
        squads_player_dict['club_country'] = player[7]
        squads_player_dict['year'] = player[8]
        # single_player.append(squads_player_dict)
        # players_list.append()
        # index += 1
        # print(player)
        players_list.append(squads_player_dict)
    # print(players_list)
    return players_list
        
# pprint(players_as_dictionaries(SQUADS_DATA))