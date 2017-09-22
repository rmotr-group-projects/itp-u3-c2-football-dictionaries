from assignment_1 import players_as_dictionaries

def players_by_country_and_position(squads_list):
    players_in_pos_by_country_dict = {}
    
    players_in_dict_list = players_as_dictionaries(squads_list)
    players_by_country_dict = players_by_criteria_dict(players_in_dict_list, "country")
    
    for key, value in players_by_country_dict.items():
        players_in_pos_dict = players_by_criteria_dict(value, "position")
        players_in_pos_by_country_dict[key] = players_in_pos_dict
    
    return players_in_pos_by_country_dict
    
def players_by_criteria_dict(players_in_dict_list, criteria):
    
    player_by_criteria_dict = {}
    
    for player in players_in_dict_list:
         criteria_val = player[criteria].strip()
         
         if player_by_criteria_dict.get(criteria_val) == None :
            players_list = [player]
            player_by_criteria_dict[criteria_val] = players_list
         else :
            player_by_criteria_dict[criteria_val].append(player)
            
    return player_by_criteria_dict