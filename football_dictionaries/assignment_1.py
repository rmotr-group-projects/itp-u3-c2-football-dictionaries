def players_as_dictionaries(squads_list):
    squads_data = []
    
    for player in squads_list:
        dictionary = {}
        dictionary['number']        = player[0]
        dictionary['position']      = player[1]
        dictionary['name']          = player[2]
        dictionary['date_of_birth'] = player[3]
        dictionary['caps']          = player[4]
        dictionary['club']          = player[5]
        dictionary['country']       = player[6]
        dictionary['club_country']  = player[7]
        dictionary['year']          = player[8]
        
        squads_data.append(dictionary)
   
    return squads_data
        
