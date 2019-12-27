def players_by_country_and_position(squads_list):
    results = {}
    for player in squads_list:
        player_dict = {
        'caps': player[4],
        'club': player[5],
        'club_country': player[7],
        'country': player[6],
        'date_of_birth': player[3],
        'name': player[2],
        'number': player[0],
        'position': player[1],
        'year': player[8],
        }
        
        position = player[1]
        country = player[6]
        
        results.setdefault(country,{})
        results[country].setdefault(position,[])        
        results[country][position].append(player_dict)
    return results