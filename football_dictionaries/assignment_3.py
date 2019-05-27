from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_country_and_position(squads_list):
  players_list = players_as_dictionaries(squads_list)
  players_sorted_by_country_position = {}
  
  for player in players_list:
    player_position = player['position'] #player.get('position', '')
    player_country = player.get('country')
    
    players_sorted_by_country_position.setdefault(player_country, {})
    players_sorted_by_country_position[player_country].setdefault(player_position, [])
    players_sorted_by_country_position[player_country][player_position].append(player)    
    
    

  return players_sorted_by_country_position