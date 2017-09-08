def players_by_position(squads_list):
    
    # Unique names of all positions in list
    position_set = set()
    
    # This will contain the players organized by position
    position_dictionary = {}
    
    key_tuple = ('number', 'position', 'name', 'date_of_birth', 'caps', 'club', 'country', 'club_country', 'year')
    
    #Find an add all unique positions to position_set 
    for players in squads_list:
        position_set.add(players[1])
    
    for position in position_set:
        position_dictionary[position] =[]
        for players in squads_list:
            if position in players:
                position_dictionary[position].append(dict(zip(key_tuple,players)))
    
    return position_dictionary
                