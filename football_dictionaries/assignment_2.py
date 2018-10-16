def transform_player_list_to_dict(player_as_list):
    player_as_dict = {
    "caps": player_as_list[4],
    "club": player_as_list[5],
    "club_country": player_as_list[7],
    "country": player_as_list[6],
    "date_of_birth": player_as_list[3],
    "name": player_as_list[2],
    "number": player_as_list[0],
    "position": player_as_list[1],
    "year": player_as_list[8],
    }
    return player_as_dict
    
def players_as_dictionaries(squads_list):
    players_list = []
    for player in squads_list:
        player_as_dict = transform_player_list_to_dict(player)
        players_list.append(player_as_dict)
    return players_list
    
def players_by_position(squads_list):
    players = {}
        
    for player_as_list in squads_list:
        player = transform_player_list_to_dict(player_as_list)
        position = player["position"]
        
        if position not in players:
            players[position] = []
        
        players[position].append(player)
    
    return players

