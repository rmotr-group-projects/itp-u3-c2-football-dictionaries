def players_as_dictionaries(squads_list):
    players = []
    for player in squads_list:
        player_dict = {
            'caps': player[4],
            'club': player[5],
            'club_country': player[7],
            'country': player[6],
            'date_of_birth': player[3],
            'name': player[2],
            'number': player[0],
            'position': player[1],
            'year': player[-1]
            }
        
        players.append(player_dict)
    return players



from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_position(squad):
    result = {}
    players_list = players_as_dictionaries(squad)
    for player in players_list:
        pos = player['position']
        result.setdefault(pos, [])
        result[pos].append(player)
    return result

from football_dictionaries.assignment_1 import players_as_dictionaries


def players_by_country_and_position(squad):
    players = players_as_dictionaries(squad)
    result = {}

    for player in players:
        pos = player['position']
        country = player['country']
        
        result.setdefault(country, {})
        result[country].setdefault(pos, [])
        result[country][pos].append(player)
    
    return result
