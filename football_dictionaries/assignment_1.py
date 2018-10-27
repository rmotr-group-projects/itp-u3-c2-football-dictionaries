def players_as_dictionaries(squads_list):
    player_dict_list = []
    stat_list = ['number', 'position', 'name', 'date_of_birth', 'caps', 'club', 'country', 'club_country', 'year']
    for player in squads_list:
        i = 0
        build = {}
        while i < len(stat_list):
            build.setdefault(stat_list[i], player[i])
            i += 1
        # build.setdefault('number', player[0])
        # build.setdefault('position', player[1])
        # build.setdefault('name', player[2])
        # build.setdefault('date_of_birth', player[3])
        # build.setdefault('caps', player[4])
        # build.setdefault('club', player[5])
        # build.setdefault('country', player[6])
        # build.setdefault('club_country', player[7])
        # build.setdefault('year', player[8])
       # build = {
        #    'number': player[0],
         #   'position': player[1],
          #  'name': player[2],
           # 'date_of_birth': player[3],
        #    'caps': player[4],
         #   'club': player[5],
         #   'country': player[6],
          #  'club_country': player[7],
           # 'year': player[8]
        #}
        player_dict_list.append(build)
    return player_dict_list
