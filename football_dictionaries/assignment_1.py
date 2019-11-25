def players_as_dictionaries(squads_list):
    
    new_squad_list = []
    keys = [
        'number',
        'position',
        'name',
        'date_of_birth',
        'caps',
        'club',
        'country',
        'club_country',
        'year'
    ]
    
    
    for player in squads_list:
        new_squad_list.append(dict(zip(keys, player)))
    
    return new_squad_list


