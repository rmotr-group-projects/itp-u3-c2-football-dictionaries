def players_by_position(squads_list):
    
    # set up new dictionary that will consist of each position as the key, with a list as its value    
    new_list = []

    for position in squads_list:
        new_list.append(position[1])
    positions = list(set(new_list))
    
    dict_position = dict.fromkeys(positions)
    
    for keys in dict_position.keys():
        dict_position[keys] = [] 

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
        
        for each_key in dict_position:
            if each_key == new_dict["position"]:
                dict_position[each_key].append(new_dict)

    return dict_position