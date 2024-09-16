def players_as_dictionaries(squads_list):
    results = []
    
    for player in squads_list:
        player_dict = {
            'number': player[0],
            'position': player[1],
            'name': player[2],
            'date_of_birth': player[3],
            'caps': player[4],
            'club': player[5],
            'country': player[6],
            'club_country': player[7],
            'year': player[8],
        }
        results.append(player_dict)
    
    return results

def players_by_position(squads_list):
    result = {}
    players = players_as_dictionaries(squads_list)
    for player in players:
        position = player['position']
        if position not in result:
            result[position] = []
        
        result.setdefault(position, [])
        list_by_position = result.get(position)
        list_by_position.append(player)
    
    return result

def players_by_country_and_position(squads_list):
    result = {}
    positions = players_by_position(squads_list)
    for position, players in positions.items():
        for player in players:
            result.setdefault(player['country'], {})
            result[player['country']].setdefault(player['position'], [])
            result[player['country']][player['position']].append(player)
    return result
