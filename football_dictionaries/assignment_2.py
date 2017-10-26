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
    

def players_by_position(squads_list):
    playersdictionaries = players_as_dictionaries(squads_list)
    positions = {}
    GK = []
    MF = []
    FW = []
    for eachplayer in playersdictionaries:
      if eachplayer['position'] == 'GK':
        GK.append(eachplayer)
      elif eachplayer['position'] == 'MF':
        MF.append(eachplayer)
      elif eachplayer['position'] == 'FW':
        FW.append(eachplayer)
    positions.setdefault('GK', GK)
    positions.setdefault('MF', MF)
    positions.setdefault('FW', FW)
    return positions
