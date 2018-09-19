from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_position(squads_list):

    position_dict = {}

    dict_list = players_as_dictionaries(squads_list)

    for player in dict_list:

        position_key = player['position']

        if position_key in position_dict:

            position_dict[position_key].append(player)

        else:

            position_dict[position_key] = [player]

    return position_dict
