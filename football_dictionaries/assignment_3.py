from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_country_and_position(squads_list):
    squads_dict = players_as_dictionaries(squads_list)
    results = {}
    
    for player in squads_dict:
        country = player['country']
        position = player['position']
        
#         if country not in results:
#             results[country] = {}
        results.setdefault(country, {})
            
#         if position not in results[country]:
#             results[country][position] = []
        results[country].setdefault(position, [])
    
        results[country][position].append(player)
    
    
    return results


'''
results = {
    'countries': {
        'positions': []
    }
}
'''