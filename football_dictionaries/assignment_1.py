def players_as_dictionaries(squads_list):
    result_list = []
    for index, item in enumerate(squads_list):
        temp_dict = {}
        temp_dict["number"] = item[0]
        temp_dict["position"] = item[1]
        temp_dict["name"] = item[2]
        temp_dict["date_of_birth"] = item[3]
        temp_dict["caps"] = item[4]
        temp_dict["club"] = item[5]
        temp_dict["country"] = item[6]
        temp_dict["club_country"] = item[7]
        temp_dict["year"] = item[8]
        result_list.append(temp_dict)
    return result_list
