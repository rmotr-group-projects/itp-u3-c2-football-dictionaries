def players_as_dictionaries(squads_list):
    new_list = []
    
    for each_list in squads_list:
        new_list.append({"caps": each_list[4], "position": each_list[1], "name": each_list[2], "date_of_birth": each_list[3], "number": each_list[0], "club": each_list[5], "country": each_list[7], "club_country": each_list[6], "year": each_list[8]})
        
    return new_list