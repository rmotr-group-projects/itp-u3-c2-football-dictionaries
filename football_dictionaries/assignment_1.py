def transform_list_player_to_dictionaries(player_as_list):
    player_dictionary = {
        'caps': player_as_list[4],
        'club': player_as_list[5],
        'club_country': player_as_list[7],
        'country': player_as_list[6],
        'date_of_birth': player_as_list[3],
        'name': player_as_list[2],
        'number': player_as_list[0],
        'position': player_as_list[1],
        'year': player_as_list[8],
        }
    return player_dictionary


def players_as_dictionaries(squads_list):
    list_of_players = []
    for player in squads_list:
        player_dictionary = transform_list_player_to_dictionaries(player)    
        list_of_players.append(player_dictionary)
    
    return list_of_players