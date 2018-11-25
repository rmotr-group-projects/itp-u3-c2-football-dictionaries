def players_as_dictionaries(squads_list):
    player_list = []
    dict_player = {}
    for player in squads_list:
        dict_player = {
        'number': player[0],
        'position': player[1],
        'name': player[2],
        'date_of_birth': player[3],
        'caps': player[4],
        'club': player[5],
        'country': player[6],
        'club_country': player[7],
        'year': player[8]
        }
        player_list.append(dict_player)
    return player_list


def players_by_position(squads_list):
        
    players_as_dict = players_as_dictionaries(squads_list)
    players_by_position = {}
    
    for player in players_as_dict:
        player_position = player['position']
        players_by_position.setdefault(player_position, [])
        players_by_position[player_position].append(player)
    
    return players_by_position

def players_by_country_and_position(squads_list):
    players_as_dict = players_as_dictionaries(squads_list)
    players_by_position = {}
    players_by_country = {}
    
    for player in players_as_dict:
        player_position = player['position']
        player_country = player['country']
        
        players_by_country.setdefault(player_country, {})        
        players_by_country[player_country].setdefault(player_position, [])
        
        players_by_country[player_country][player_position].append(player)
    


    return players_by_country
