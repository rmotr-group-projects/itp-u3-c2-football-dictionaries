result = {
    'Argentina': {},
    'Belgium': {},
    'Brazil': {},
    'South Korea': {},
}

def players_by_country_and_position(squads_list):
    for player in squads_list:
        new_player = {
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
        
        country = new_player['country']
        position = new_player['position']
        
        if country in result:
            result[country].setdefault(position, [])
            result[country][position].append(new_player)

    return result
    
