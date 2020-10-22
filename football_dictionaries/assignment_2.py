from .assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    results = {}
    players_dict = players_as_dictionaries(squads_list) 
    for player in players_dict:
        results.setdefault(player['position'],[])
        results[player['position']].append(player)
        
    return results