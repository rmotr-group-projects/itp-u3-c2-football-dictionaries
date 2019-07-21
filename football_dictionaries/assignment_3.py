def players_by_country_and_position(data):
    results = {}
    
    playerdict = players_as_dictionaries(data)
    
    
    
    for player in playerdict:
        country = player['country']
        position = player['position']
        
        results.setdefault(country, {})
        results[country].setdefault(position, [])
        results[country][position].append(player)
        
    return results

