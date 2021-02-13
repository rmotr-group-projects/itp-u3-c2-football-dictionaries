def players_by_country_and_position(squads_list):
    squad_dict = {}
    
    for player in squads_list:
        country = player[6]
        position = player[1]
        squad_dict.setdefault(country, {})
        squad_dict[country].setdefault(position, [])
        player_dict = {
                    'number': player[0],
                    'position': player[1],
                    'name': player[2],
                    'date_of_birth': player[3],
                    'caps': player[4],
                    'club': player[5],
                    'country': player[6],
                    'club_country': player[7],
                    'year': player[8]
                     }
        squad_dict[country][position].append(player_dict)
        
    return squad_dict
