def players_as_dictionaries(squads_list):
    squads_data = []
    player_data = {}
    
    for player in squads_list:
        player_data = {
            'caps': player[4],
            'club': player[-4],
            'club_country': player[-2],
            'country': player[-3],
            'date_of_birth': player[3],
            'name': player[2],
            'number': player[0],
            'position': player[1],
            'year': player[-1]        
        }
        squads_data.append(player_data)
    return squads_data
        
