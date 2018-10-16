def players_as_dictionaries(squads_list):
    players_list = []

    key_tuple = ('number', 'position', 'name', 'date_of_birth', 'caps', 'club', 'country', 'club_country', 'year')

    for players in squads_list:
    	dict_of_players_stats = dict(zip(key_tuple,players))
    	players_list.append(dict_of_players_stats)

    return players_list
