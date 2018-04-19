def players_as_dictionaries(squads_list):
    result = []
    
    keys = ['number',
    'position',
    'name',
    'date_of_birth',
    'caps',
    'club',
    'country',
    'club_country',
    'year']
    
    for squad in squads_list:
        item_dict ={}
        for key,item in zip(keys,squad):
            item_dict[key] = item
        result.append(item_dict)
    
    return result
