
def player_list_to_dict(list_of_player):
    player_dictionaries = {
        'caps': list_of_player[4],
        'club': list_of_player[5],
        'club_country': list_of_player[7],
        'country': list_of_player[6],
        'date_of_birth': list_of_player[3],
        'name': list_of_player[2],
        'number': list_of_player[0],
        'position': list_of_player[1],
        'year': list_of_player[8]
    }
    return player_dictionaries

def players_by_position(squads_list):
    playersByPosition = {
        "GK": [],
        "MF": [],
        "FW": [],
       
    }
    for player_list in squads_list:
        player_dict = player_list_to_dict(player_list)
        player_position = player_dict['position']
        playersByPosition[player_position].append(player_dict)
    return playersByPosition
      
    
    return players


