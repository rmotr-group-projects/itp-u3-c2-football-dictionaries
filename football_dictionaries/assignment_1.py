def players_as_dictionaries(squads_list):
    result = []
    for individual in squads_list:
        squad_dict = {
            'caps' : individual[4],
            'club' : individual[5],
            'club_country' : individual[7],
            'country' : individual[6],
            'date_of_birth' : individual[3],
            'name' : individual[2],
            'number' : individual[0],
            'position' : individual[1],
            'year' : individual[8]
        }
        result.append(squad_dict)
    return result
    
        
    
        
