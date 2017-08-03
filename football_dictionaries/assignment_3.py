from utils import convert_player_to_dict
def players_by_country_and_position(squads_list):
  players_by_country = {}

  for player in squads_list:
    my_dict = convert_player_to_dict(player)

    player_country = my_dict["country"]
    player_position = my_dict["position"]
    
    if player_country not in players_by_country:
        players_by_country[player_country] = {}
    if player_position not in players_by_country[player_country]:
        players_by_country[player_country][player_position] = []
    players_by_country[player_country][player_position].append(my_dict)
  return players_by_country