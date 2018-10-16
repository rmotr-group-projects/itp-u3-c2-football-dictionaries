from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_position(squads_list):

    players = players_as_dictionaries(squads_list)
    
    results = {
        'GK' : [],
        'MF' : [],
        'FW' : []
    }

    for individual_player in players:
        results[individual_player['position']].append(individual_player)
        
    return results
    