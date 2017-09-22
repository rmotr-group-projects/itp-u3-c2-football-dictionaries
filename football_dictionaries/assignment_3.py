def players_by_country_and_position(squads_list):
    
    position_list = []
    country = {}

    for each_list in squads_list:
        new_dict = {"caps": each_list[4],
        "position": each_list[1], 
        "name": each_list[2], 
        "date_of_birth": each_list[3], 
        "number": each_list[0], 
        "club": each_list[5], 
        "country": each_list[7], 
        "club_country": each_list[6], 
        "year": each_list[8]}
    
        club_country = each_list[6]
        player_position = each_list[1]

        if club_country in country:
        	if player_position in country[club_country]:
        		country[club_country][player_position].append(new_dict)
        	else:
        		country[club_country][player_position] = [new_dict]
        else:
        	country[club_country] = {player_position : [new_dict]}
    
    return country