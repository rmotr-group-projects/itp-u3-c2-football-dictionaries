

def players_as_dictionaries(squads_list):
    result = []
    for player in squads_list:
        empty_dict = {}
        
        for index,item in enumerate(player):
            key_list = [
            "number",
            "position",
            "name",
            "date_of_birth",
            "caps",
            "club",
            "country",
            "club_country",
            "year"
            ]
            key = key_list[index]
            empty_dict[key] = item
            if index == 8:
                result.append(empty_dict)        
    return result
            
    


