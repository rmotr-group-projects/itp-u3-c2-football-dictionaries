def players_as_dictionaries(squads_list):
    list_of_players = []
    
    for players in squads_list:
        dict_of_players_stats ={}
        dict_of_players_stats['number'] = players[0]
        dict_of_players_stats['position'] = players[1]
        dict_of_players_stats['name'] = players[2]
        dict_of_players_stats['date_of_birth'] = players[3]
        dict_of_players_stats['caps'] = players[4]
        dict_of_players_stats['club'] = players[5]
        dict_of_players_stats['country'] = players[6]
        dict_of_players_stats['club_country'] = players[7]
        dict_of_players_stats['year'] = players[8]
        list_of_players.append(dict_of_players_stats)
    
    return list_of_players
