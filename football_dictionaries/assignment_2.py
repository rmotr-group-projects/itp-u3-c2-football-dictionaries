def players_by_position(squads_list):
    
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
    
    output_list = []
    for player in squads_list:
        output_list.append(dict(zip(field_list, list(player[:]))))
    
    output_dict = dict()
    
    for player in output_list:
        if player["position"] not in output_dict:
            output_dict[player["position"]] = []
        output_dict[player["position"]].append(player)
    
    return output_dict
    