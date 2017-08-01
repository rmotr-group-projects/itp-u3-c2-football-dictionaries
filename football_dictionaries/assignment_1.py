def players_as_dictionaries(squads_list):
  my_list = []
  for squads in squads_list:
    my_dict = {'number': squads[0],
    'position': squads[1],
    'name':   squads[2],
    'date_of_birth': squads[3],
    'caps': squads[4],
    'club': squads[5],
    'country': squads[6],
    'club_country': squads[7],
    'year': squads[8]
    }
    my_list.append(my_dict)
  return my_list