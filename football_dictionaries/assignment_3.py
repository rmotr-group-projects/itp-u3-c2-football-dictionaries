def players_by_country_and_position(squads_list):
    players_by_country = {}
    for i in squads_list:
        player_info= {
        "number" : i[0],
        "position" : i[1],
        "name" : i[2],
        "date_of_birth" : i[3],
        "caps" : i[4],
        "club" : i[5],
        "country" : i[6],
        "club_country" : i[7],
        "year" : i[8]
        }
        players_by_country[player_info['country']] = players_by_country.get(player_info['country'],{})
        
        if player_info["position"] not in players_by_country[player_info["country"]].keys():
            players_by_country[player_info["country"]].update({player_info["position"]:[]})
        
        players_by_country[player_info['country']][player_info["position"]].append(player_info)
        
    return players_by_country