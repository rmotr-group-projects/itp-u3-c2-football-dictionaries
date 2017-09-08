from utils import convert_player_to_dict
def players_as_dictionaries(squads_list):
  my_list = []
  for player in squads_list:
    my_dict = convert_player_to_dict(player)
    my_list.append(my_dict)
  return my_list