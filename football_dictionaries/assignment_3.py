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

def players_by_country_and_position(squads_list):
    players = players_as_dictionaries(squads_list)
    return_dict = {}
    for player in players:
        if return_dict.get(player['country']) is not None:
            if return_dict.get(player['country']).get(player['position']) is not None:
                return_dict[player['country']][player['position']].append(player)
            else:
                return_dict[player['country']][player['position']] = [player]
        else:
            new_position_dict = {player['position'] : [player]}
            return_dict[player['country']] = new_position_dict
    return return_dict