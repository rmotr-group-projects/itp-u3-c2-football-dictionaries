def players_as_dictionaries(squads_list):
  my_list = []
  for value in squads_list:
    my_dict = {'number': value[0], 'position': value[1], 'name': value[2], 'date_of_birth': value[3], 'caps': value[4], 'club': value[5], 'country': value[6], 'club_country': value[7],'year': value[8]}
    my_list.append(my_dict)
  return my_list