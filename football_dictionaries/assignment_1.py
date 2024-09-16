def players_as_dictionaries(squads_list):
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
    return result
