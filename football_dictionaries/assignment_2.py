from football_dictionaries.assignment_1 import players_as_dictionaries


def players_by_position(squads_list):
    imported_players = players_as_dictionaries(squads_list)
    player_position_dict = {}
    for player in imported_players:
        position = player['position']
        player_position_dict.setdefault(position, [])
        player_position_dict[position].append(player)
    return player_position_dict