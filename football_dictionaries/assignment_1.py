def players_as_dictionaries(squads_list):
    #iterate over input while creating generic dictionaries from set(keys_list) values
    #fill dict(squad) with the input from player in squads_list
    #append to list(players) 
    #return list(players)
    players = []
    keys_list = ['number', 'position', 'name', 'date_of_birth', 'caps', 'club', 'country', 'club_country', 'year']
    
    for player in squads_list:
            squad = {}
            index = 0
            squad = dict.fromkeys(set(keys_list))
            for stat in player:
                squad[keys_list[index]] = player[index]
                index += 1
            players.append(squad)
    return players   