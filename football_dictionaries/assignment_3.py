def players_as_dictionaries(squads_list):
    results = []
    for players in squads_list:
        player = {'number': players[0],
            'position': players[1],
            'name': players[2],
            'date_of_birth': players[3],
            'caps': players[4],
            'club': players[5],
            'country': players[6],
            'club_country': players[7],
            'year': players[8],}
        results.append(player)
    return results

def players_by_country_and_position(squads_list):
    players_dict = players_as_dictionaries(squads_list)
    results = {}
    
    for player in players_dict:
        country = player['country']
        position = player['position']
        results.setdefault(country,{})
        results[country].setdefault(position,[])
        results[country][position].append(player)
    return results
