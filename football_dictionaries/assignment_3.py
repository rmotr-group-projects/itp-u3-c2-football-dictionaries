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


def players_by_position(squad_list):
    new_dict = {}
    player_dict = players_as_dictionaries(squad_list)
    for player in player_dict:
        
        pos = player['position']
        new_dict.setdefault(pos, [])
        new_dict[pos].append(player)
    return new_dict



def players_by_country_and_position(squads_list):
    players_as_dict = players_as_dictionaries(squads_list)
    country_dict = {}
    for player in players_as_dict:
        country = player['country']
        position = player['position']
        country_dict.setdefault(country, {})
        country_dict[country].setdefault(position, [])
        country_dict[country][position].append(player)
        
    
    return country_dict





    