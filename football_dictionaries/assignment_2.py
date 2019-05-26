import football_dictionaries.assignment_1 as asd

def players_by_position(squads_list):
    list_of_players = asd.players_as_dictionaries(squads_list)
    player_dict = {}
    for player in list_of_players: 
        player_dict.setdefault(player['position'],[])
        player_dict[player['position']].append(player)
    return player_dict
    
 
