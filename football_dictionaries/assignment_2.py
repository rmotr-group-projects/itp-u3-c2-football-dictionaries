def players_by_position(squads_list):
    
    result = {}
    for player in squads_list:
        result.setdefault (player[1],[])    
    print(result)        
    for player in squads_list:
        result[player[1]].append({
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
    return result
   

