from football_dictionaries.assignment_1 import players_as_dictionaries
def players_by_position(squads_list):
    players = players_as_dictionaries(squads_list)
    new_players_dict = {}
    
    for player in players:
        player_position = player['position']
        new_players_dict.setdefault(player_position, [])
        new_players_dict[player_position].append(player)
    
    return new_players_dict
    
    
    
    
    
