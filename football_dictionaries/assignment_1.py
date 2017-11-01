def players_as_dictionaries(squads_list):
    
    dict_items = {
        1 : "number",
        2 : "position",
        3 : "name",
        4 : "date_of_birth",
        5 : "caps",
        6 : "club",
        7 : "country",
        8 : "club_country",
        9 : "year"
    }
    
    squads_list_to_dict = []

    for squad in squads_list:
        squad_dict = {}
        for item in range(0, len(squad)):
            squad_dict[dict_items[item+1]] = squad[item]
        squads_list_to_dict.append(squad_dict)
    
    return squads_list_to_dict