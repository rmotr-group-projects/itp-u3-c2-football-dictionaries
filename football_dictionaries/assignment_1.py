def players_as_dictionaries(squads_list):
    # create a list of dictionaries
    data = ['number', 'position', 'name', 'date_of_birth', 'caps', 'club', 'country', 'club_country', 'year']
    
    profiles = []
    
    for player in squads_list:
        players_dict = {}
        index = 0
        for eachinfo in player:
            players_dict[data[index]] = eachinfo
            index += 1
        profiles.append(players_dict)
    return profiles