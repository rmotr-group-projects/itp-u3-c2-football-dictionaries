def players_as_dictionaries(squads_list):
    results = []
    
    for player in squads_list:
        player_dictionary = {
            'caps': player[4],
            'club': player[5], 
            'club_country': player[-2], 
            'country': player[-3], 
            'date_of_birth': player[3],
            'name': player[2], 
            'number': player[0], 
            'position': player[1],
            'year': player[-1], 
        }
        
        results.append(player_dictionary)
    
    return results
