from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    squads_dictionary = players_as_dictionaries(squads_list)
    
    results = {}
    
    for player in squads_dictionary:
        position = player['position']
        
        if position not in results:
            results[position] = []
        
        results[position].append(player)
    
    
    return results



'''
results = {
    'goalkeepers': []
}
''' 