def players_as_dictionaries(squads_list):
  players_by_position = {
    "GK" : [],
    "DF" : [],
    "MF" : [],
    "FW" : []
  }
  
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

    if(squads[1] == "GK"):
      players_by_position["GK"].append(my_dict)

    if(squads[1] == "DF"):
      players_by_position["DF"].append(my_dict)

    if(squads[1] == "MF"):
      players_by_position["MF"].append(my_dict)

    if(squads[1] == "FW"):
      players_by_position["FW"].append(my_dict)

  return players_by_position


