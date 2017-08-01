def players_as_dictionaries(squads_list):
  playalist = []
  for _ in range(len(squads_list)):
    playalist.append({})
  for i in range(len(squads_list)):
    playalist[i]['number']=squads_list[i][0]
    playalist[i]['position']=squads_list[i][1]
    playalist[i]['name']=squads_list[i][2]
    playalist[i]['date_of_birth']=squads_list[i][3]
    playalist[i]['caps']=squads_list[i][4]
    playalist[i]['club']=squads_list[i][5]
    playalist[i]['country']=squads_list[i][6]
    playalist[i]['club_country']=squads_list[i][7]
    playalist[i]['year']=squads_list[i][8]
  return playalist  

def players_by_country_and_position(squads_list):
  player_by_country = {}
  for player in players_as_dictionaries(squads_list):
    if player["country"] not in player_by_country:
      player_by_country[player["country"]] = {}
    if player["position"] not in player_by_country[player["country"]]:
      player_by_country[player["country"]][player["position"]] = []
    player_by_country[player["country"]][player["position"]].append(player)
  return player_by_country