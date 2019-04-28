squad_keys = ['number', 'position', 'name', 'date_of_birth', 'caps', 'club', 'country', 'club_country', 'year']

def item_to_dict(data):
    counter = 0    
    squad_dict = {}
    for item in data: 
        number_value = item
        squad_dict.setdefault(squad_keys[counter], number_value)
        counter += 1
    return(squad_dict)
    
def players_as_dictionaries(squads_list):
    final_list = []
    for item in squads_list:
        temp_data = item
        single_dict = item_to_dict(temp_data)
        final_list.append(single_dict)

    return final_list


