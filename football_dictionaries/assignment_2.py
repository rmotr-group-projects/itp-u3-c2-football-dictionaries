from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
  squads_dict = players_as_dictionaries(squads_list)
  
  players_by_position_dict = {}

  for squad in squads_dict:
      position = squad['position']
      if position not in players_by_position_dict:
          players_by_position_dict[position] = [squad] 
      else:
          players_by_position_dict[position].append(squad) 
  
  return players_by_position_dict
