def players_as_dictionaries(squads_list):
    new_squads_list = []
    
    for squad in squads_list:
        squads_dict = {}
        squads_dict['caps'] = squad[4]
        squads_dict['club'] = squad[5]
        squads_dict['club_country'] = squad[7]
        squads_dict['country'] = squad[6]
        squads_dict['date_of_birth'] = squad[3]
        squads_dict['name'] = squad[2]
        squads_dict['number'] = squad[0]
        squads_dict['position'] = squad[1]
        squads_dict['year'] = squad[8]
        new_squads_list.append(squads_dict)
        
    return new_squads_list



     



