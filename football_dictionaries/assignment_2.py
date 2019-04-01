        

def players_by_position(squads_list):
    players = {}

    for player_as_list in squads_list:
        player = transform_list_player_to_dict(player_as_list)
        position = player['position'] 
        
        players.setdefault(position, [])
            
        list_by_position = players.get(position)
        list_by_position.append(player)
    
    return players