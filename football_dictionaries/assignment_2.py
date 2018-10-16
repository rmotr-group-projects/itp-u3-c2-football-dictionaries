from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    result = {}
    
    for player in players_as_dictionaries(squads_list):
        
        result.setdefault(player['position'], [])
        result[player['position']].append(player)
        
    return result        
