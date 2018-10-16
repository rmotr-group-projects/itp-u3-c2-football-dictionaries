def players_as_dictionaries(squads_list):
    result = []
    for player in squads_list:
        temp_dict = {}
        temp_dict['number'] = player[0]
        temp_dict['position'] = player[1]
        temp_dict['name'] = player[2]
        temp_dict['date_of_birth'] = player[3]
        temp_dict['caps'] = player[4]
        temp_dict['club'] = player[5]
        temp_dict['country'] = player[6]
        temp_dict['club_country'] = player[7]
        temp_dict['year'] = player[8]
        result.append(temp_dict)
    
    return result

