def players_as_dictionaries(squads_list):
    dict_master = []
    dict_order = ["number", "position", "name", "date_of_birth", "caps","club","country","club_country","year"]
    for player in squads_list:
        temp_dict = {}
        for value,key in zip(player, dict_order):
            temp_dict.update({key:value})
        dict_master.append(temp_dict)
    return dict_master