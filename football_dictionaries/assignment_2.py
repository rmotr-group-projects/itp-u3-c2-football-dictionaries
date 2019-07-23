def players_by_position(squads_list):
    result = {}
    for individual in squads_list:
        result.setdefault(individual[1],[])
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
        result[individual[1]].append(squad_dict)
    return result
    

'''result{ 'position' : [{players}]}'''