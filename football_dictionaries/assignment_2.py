from .assignment_1 import transform_list_player_to_dictionary
def players_by_position(squads_list):
    players= {}
        
    
    
    for player_as_list in squads_list:
        player= transform_list_player_to_dictionary(player_as_list)
        position= player["position"]
        players.setdefault(position,[])
        players[position].append(player)
    return players


