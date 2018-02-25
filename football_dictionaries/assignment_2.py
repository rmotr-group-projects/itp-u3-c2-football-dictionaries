from assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    players_list = players_as_dictionaries(squads_list)
    
    result={}
    
    for player in players_list:
        position=player['position']
        
        result.setdefault(position,[])
        result[position].append(player)
    
    return result
