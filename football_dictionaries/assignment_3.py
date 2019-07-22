
def players_as_dictionaries(data):
    playerslist = []
    
    for player in data:
        playersdict = {
    'number': player[0],
    'position': player[1],
    'name': player[2],
    'date_of_birth': player[3],
    'caps': player[4],
    'club': player[5],
    'country': player[6],
    'club_country': player[7],
    'year': player[8],
}
        playerslist.append(playersdict)
    
    return playerslist


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

