def player_as_dict(player_list):
    player_dict = {
        'number': player_list[0],
        'position': player_list[1],
        'name': player_list[2],
        'date_of_birth': player_list[3], 
        'caps': player_list[4], 
        'club': player_list[5],
        'club_country':  player_list[7],
        'country': player_list[6],
        'year': player_list[8]
    }
    return player_dict

def players_as_dictionaries(squads_list):
    player_list = []
    for player in squads_list:
        player_dict = player_as_dict(player)
        player_list.append(player_dict) 

    return player_list
