def transform_list_player_to_dict(squads_list):
    squads_dict = {            
            'caps': squads_list[4],
            'club': squads_list[5],
            'club_country': squads_list[7],
            'country': squads_list[6],
            'date_of_birth': squads_list[3],
            'name': squads_list[2],
            'number': squads_list[0],
            'position': squads_list[1],
            'year': squads_list[8],
        }
    return squads_dict


def players_as_dictionaries(squads_list):
    squads_data = []
    for player in squads_list:
        squads_dict = transform_list_player_to_dict(player)
        squads_data.append(squads_dict)
    return squads_data 


def players_by_country_and_position(squads_list):
    squads_dict = players_as_dictionaries(squads_list)
    country_and_position = {}
    
    for player in squads_dict:
        country = player['country']
        position = player['position']
        country_and_position.setdefault(country, {}) 
        country_and_position[country].setdefault(position, [])
        country_and_position[country][position].append(player)
            
    return country_and_position 
