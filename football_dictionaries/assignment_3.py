def players_by_country_and_position(squads_list):
    empty_list = []
    #empty_dict = {}
    for list_item in squads_list:
        empty_dict = {}
        #for list_item in lists:
        empty_dict["number"] = list_item[0]
        empty_dict["position"] = list_item[1]
        empty_dict["name"] = list_item[2]
        empty_dict["date_of_birth"] = list_item[3]
        empty_dict["caps"] = list_item[4]
        empty_dict["club"] = list_item[5]
        empty_dict["country"] = list_item[6]
        empty_dict["club_country"] = list_item[7]
        empty_dict["year"] = list_item[8]
        empty_list.append(empty_dict)
    result = empty_list
    new_list = []
    for dictionaries in result:
        if dictionaries["country"] not in new_list:
            new_list.append(dictionaries["country"])
    print(new_list)
    country_position_dict = {}
    for country in new_list:
        country_position_list = []
        
        for players in result:
            if players["position"] not in country_position_list and players["country"] == country:
                country_position_list.append(players["position"])

        sub_country_position_dict = {}
        print(country_position_list)
        for positions in country_position_list:
            player_list_for_country_position = []
            for players in result:
                if players["position"] == positions and players["country"] == country:
                    player_list_for_country_position.append(players)
                    print(player_list_for_country_position)
            sub_country_position_dict[positions] = player_list_for_country_position
            country_position_dict[country] = sub_country_position_dict
    print(country_position_dict)
    return country_position_dict
        
            
            
#             if players["country"] == country:
#                 if country in country_position_dict:
                    
    
    
    
    
    
    
    
    
#     new_list2 = []
#     for dictionaries in result:
#         if dictionaries["position"] not in new_list2:
#             new_list2.append(dictionaries["position"])
#     print(new_list2)
#     new_dict = {}
#     for countries in new_list:
#         another_new_dict = {}
    
#         for positions in new_list2:
            
#             another_new_list = []
#             for dictionaries in result:
#                 if dictionaries["position"] == positions and dictionaries["country"] == countries:
#                     another_new_list.append(dictionaries)
                
#             another_new_dict[positions] = another_new_list
#         new_dict[countries] = another_new_dict
#     new_result = new_dict
#     print(new_result)
#     return new_result
        
        
        