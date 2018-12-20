def list_to_dict(players_as_list):
    player_dict = {
        'caps': players_as_list[4],
        'club': players_as_list[5],
        'club_country': players_as_list[7],
        'country': players_as_list[6], 
        'date_of_birth': players_as_list[3],
        'name': players_as_list[2],
        'number': players_as_list[0],
        'position': players_as_list[1],
        'year': players_as_list[8]
    }
    return player_dict

def players_as_dictionaries(squads_list):
    result = []
    for player in squads_list:
        players_dict = list_to_dict(player) 
        result.append(players_dict)
    return result
        
   





