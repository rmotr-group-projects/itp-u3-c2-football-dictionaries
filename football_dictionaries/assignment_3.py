from football_dictionaries.assignment_2 import players_by_position

def players_by_country_and_position(squads_list):
    
    players = players_by_position(squads_list)
    
    result = {
        'Argentina': {
            'GK' : [],
            'FW' : []
        },
        'Belgium': {
            'GK' : [],
            'MF' : []
        },
        'Brazil': {
            'MF' : []
        },
        'South Korea': {
            'FW' : []
        }
    }
    
    for position in players:
        for player in players[position]:
            result[player['country']][player['position']].append(player)
    
    return result
    