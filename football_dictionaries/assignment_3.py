def players_as_dictionaries(squads_list):
    mainlist = []
    for playerinlist in squads_list:
      player = {}
      player.setdefault('number', playerinlist[0])
      player.setdefault('position', playerinlist[1])
      player.setdefault('name', playerinlist[2])
      player.setdefault('date_of_birth', playerinlist[3])
      player.setdefault('caps', playerinlist[4])
      player.setdefault('club', playerinlist[5])
      player.setdefault('country', playerinlist[6])
      player.setdefault('club_country', playerinlist[7])
      player.setdefault('year', playerinlist[8])
      mainlist.append(player)
    return mainlist
    
def players_by_country_and_position(squads_list):
    playersasdictionaries = players_as_dictionaries(squads_list)
    result = {}
    for eachplayer in playersasdictionaries:
        country = eachplayer['country']
        position = eachplayer['position']
        if country not in result:
            result[country] = {}
        if position not in result[country]:
            result[country][position] = []
        result[country][position].append(eachplayer)
    return result
    

    