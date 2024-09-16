def players_by_position(squads_list):
    pass
    empty_list = []
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
    result1 = empty_list
    new_list = []
    for dictionaries in result1:
        if dictionaries["position"] not in new_list:
            new_list.append(dictionaries["position"])
    print(new_list)
    new_dict = {}
    for items in new_list:
        another_new_list = []
        for dictionaries in result1:
            if dictionaries["position"] == items:
                another_new_list.append(dictionaries)
        new_dict[items] = another_new_list
    new_result = new_dict
    return new_result
