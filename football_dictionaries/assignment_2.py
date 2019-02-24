def players_as_dictionaries(player_list):
    result = []
    for item in player_list:
        player_dict = {
            'number': item[0],
            'position': item[1],
            'name': item[2],
            'date_of_birth': item[3],
            'caps': item[4],
            'club': item[5],
            'country': item[6],
            'club_country': item[7],
            'year': item[8],
            
        }
        result.append(player_dict)
    return result


def players_by_position(squads_list):
    new_dict = {}
    player_dict = players_as_dictionaries(squads_list)
    for player in player_dict:
        
        pos = player['position']
        new_dict.setdefault(pos, [])
        new_dict[pos].append(player)
    return new_dict
