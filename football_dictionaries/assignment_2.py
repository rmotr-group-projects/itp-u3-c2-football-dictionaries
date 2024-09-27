from football_dictionaries.assignment_1 import players_as_dictionaries 

def players_by_position(squads_list):
    final_dict = {}
    player_list_of_dictionaries = players_as_dictionaries(squads_list)
    
    for player in player_list_of_dictionaries:
        position = player["position"]
        final_dict.setdefault(position, [])
        final_dict[position].append(player)
    return final_dict 