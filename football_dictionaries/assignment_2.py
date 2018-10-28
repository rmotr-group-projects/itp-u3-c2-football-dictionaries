from football_dictionaries.assignment_1 import players_as_dictionaries

# def position_sort(position_dict, player, position):
#     if player['position'] == position:
#         position_dict[position].append(player)
#     return position_dict

def players_by_position(squads_list):
    position_dict = {}
    player_dict_list = players_as_dictionaries(squads_list)
    for player in player_dict_list:
            position = player['position']
            position_dict.setdefault(position, [])
            position_dict[position].append(player)
    # position_list = ['GK', 'FW', 'MF']
    # for position in position_list:
    #     position_dict.setdefault(position, [])
    # for player in player_dict_list:
    #     for position in position_list:
    #         position_dict = position_sort(position_dict, player, position)
    return position_dict