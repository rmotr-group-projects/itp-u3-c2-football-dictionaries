def players_as_dictionaries(squads_list):
    list_of_player_dict = []
    
    for item in squads_list:
        player_dict = {
            'number': item[0],
            'position': item[1],
            'name': item[2],
            'date_of_birth':item[3],
            'caps':item[4],
            'club':item[5],
            'country':item[6],
            'club_country':item[7],
            'year':item[8]
            }
        list_of_player_dict.append(player_dict)
    return list_of_player_dict
                         
           
