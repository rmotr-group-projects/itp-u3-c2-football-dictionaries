
def players_as_dictionaries(squads_list):
    final_list = []
    for item in squads_list:
        player = {}
        player['number'] = item[0]
        player['position'] = item[1]
        player['name'] = item[2]
        player['date_of_birth'] = item[3]
        player['caps'] = item[4]
        player['club'] = item[5]
        player['country'] = item[6]
        player['club_country'] = item[7]
        player['year'] = item[8]
        final_list.append(player)

    return final_list