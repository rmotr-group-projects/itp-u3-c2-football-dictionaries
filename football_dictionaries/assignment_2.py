from utils import convert_player_to_dict
def players_by_position(squads_list):
  players_by_position = {}

  for player in squads_list:
    my_dict = convert_player_to_dict(player)

    player_position = my_dict["position"]
    if player_position not in players_by_position:
        players_by_position[player_position] = []
    players_by_position[player_position].append(my_dict)

  return players_by_position


