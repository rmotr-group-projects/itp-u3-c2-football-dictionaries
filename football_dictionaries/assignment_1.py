def transform_list_to_dict(player_as_list):
    player_dict = {
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
    return player_dict

def players_as_dictionaries(squads_list):
    list_of_dicts = []
    for player in squads_list:
        player_as_dict = transform_list_to_dict(player)
        list_of_dicts.append(player_as_dict)
    return list_of_dicts