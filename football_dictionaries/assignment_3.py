def players_by_country_and_position(squads_list):
    result = {}
    
    expected_countries = ['Argentina', 'Belgium', 'Brazil', 'South Korea']
    
    for player in squads_list:
        result.setdefault(player[6],{})
    
    for player in squads_list:
        result[player[6]].setdefault(player[1],[])
        if player[6] in expected_countries:
            result[player[6]][player[1]].append({
                   'number': player[0],
                   'position': player[1],
                   'name': player[2],
                   'date_of_birth': player[3],
                   'caps': player[4],
                   'club': player[5],
                   'country': player[6],
                   'club_country': player[7],
                   'year': player[8]
               })
    print(result['Argentina'])           
    return result
