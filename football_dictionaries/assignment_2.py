def players_by_position(squads_list):
  players_by_position = {}

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

    player_position = my_dict["position"]
    if player_position not in players_by_position:
        players_by_position[player_position] = []
    players_by_position[player_position].append(my_dict)

  return players_by_position


