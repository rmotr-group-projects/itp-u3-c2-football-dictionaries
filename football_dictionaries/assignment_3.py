def players_by_country_and_position(squads_list):
    a_list = []
    for player in squads_list:
        a_list.append({
            'number': player[0],
            'position': player[1],
            'name': player[2],
            'date_of_birth': player[3],
            'caps': player[4],
            'club': player[5],
            'country': player[6],
            'club_country': player[7],
            'year': player[8],
        })

    result = {}    
    for player in a_list:
        position = player['position']
        country = player['country']
        result.setdefault(country, {})
        result[country].setdefault(position, [])
        result[country][position].append(player)
        
    return result
    
