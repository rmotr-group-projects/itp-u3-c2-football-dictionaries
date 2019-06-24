def players_as_dictionaries(squads_list):
    squads_data = []
    for data in range(len(squads_list)):
        a_dict = {
             'number': squads_list[data][0],
             'position': squads_list[data][1],
                'name': squads_list[data][2],
          'date_of_birth': squads_list[data][3],
                 'caps': squads_list[data][4],
                'club': squads_list[data][5],
              'country': squads_list[data][6],
          'club_country': squads_list[data][7],
                   'year': squads_list[data][8],}
        squads_data.append(a_dict)
    return squads_data