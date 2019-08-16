from football_dictionaries.assignment_1 import players_as_dictionaries


def players_by_position(squads_list):
    # players as dict
    squads_list_as_dict = players_as_dictionaries(squads_list)
    result_player_x_position = {}


    for player in squads_list_as_dict:
        position = player['position']
        result_player_x_position.setdefault(position, [])
        result_player_x_position[position].append(player)
    
    return result_player_x_position




