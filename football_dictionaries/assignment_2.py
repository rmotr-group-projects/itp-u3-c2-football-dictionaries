


from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    squads_data = players_as_dictionaries(squads_list)
    result = {}
    
    for player in squads_data:
        position = player['position']
        result.setdefault(position, [])
        result[position].append(player)
        
    return result
        
