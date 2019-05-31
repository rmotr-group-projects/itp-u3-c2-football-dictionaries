def players_as_dictionaries(squads_list):
    result = []
    for player in squads_list:
        playerinfo = {}
        playerinfo['number'] = player[0]
        playerinfo['position'] = player[1]
        playerinfo['name'] = player[2]
        playerinfo['date_of_birth'] = player[3]
        playerinfo['caps'] = player[4]
        playerinfo['club'] = player[5]
        playerinfo['country'] = player[6]
        playerinfo['club_country'] = player[7]
        playerinfo['year'] = player[8]
        result.append(playerinfo)
    return result
