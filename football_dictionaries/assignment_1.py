def players_as_dictionaries(squads_list):
    player_dict_list = []
    stat_list = ['number', 'position', 'name', 'date_of_birth', 'caps', 'club', 'country', 'club_country', 'year']
    for player in squads_list:
        i = 0
        build = {}
        while i < len(stat_list):
            build.setdefault(stat_list[i], player[i])
            i += 1
        player_dict_list.append(build)
    return player_dict_list
