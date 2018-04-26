from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_country_and_position(squads_list):
    '''Organize football players by their home country and their position'''
    
    player_background = {}
    players = players_as_dictionaries(squads_list)
    for player in players:
        country = player['country']
        position = player['position']
        player_background.setdefault(country, {})
        player_background[country].setdefault(position, [])
        
        player_background[country][position].append(player)
        
    return player_background    
