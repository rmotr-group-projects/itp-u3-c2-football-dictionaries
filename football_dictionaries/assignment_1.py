def players_as_dictionaries(squads_list):
    field_list = ['number', 
                  'position',
                  'name',
                  'date_of_birth',
                  'caps',
                  'club', 
                  'country', 
                  'club_country',
                  'year'
                 ]
    output = []
    for player in squads_list:
        output.append(dict(zip(field_list, list(player[:]))))
    
    return output 