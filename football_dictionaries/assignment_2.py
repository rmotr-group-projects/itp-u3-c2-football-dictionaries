def players_as_dictionaries(squads_list):
    squads_dict_list = []
    for squad in squads_list:
        squads_dict_list.append({
                'number': squad[0],
                'position': squad[1],
                'name': squad[2],
                'date_of_birth': squad[3],
                'caps': squad[4],
                'club': squad[5],
                'country': squad[6],
                'club_country': squad[7],
                'year': squad[8],
            })
    return squads_dict_list

def players_by_position(squads_list):
    players = players_as_dictionaries(squads_list)
    position_dict = {}
    for player in players:
        if position_dict.get(player['position']) == None:
            position_dict[player['position']] = [player]
        else:
            position_dict[player['position']].append(player)
    return position_dict

