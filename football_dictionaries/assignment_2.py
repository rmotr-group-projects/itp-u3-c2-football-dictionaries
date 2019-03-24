from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    players_by_position_dict={}
    players_dict=players_as_dictionaries(squads_list)
    for player in players_dict:
        players_by_position_dict.setdefault(player['position'],[])
        players_by_position_dict[player['position']].append(player)
    return players_by_position_dict    
        
