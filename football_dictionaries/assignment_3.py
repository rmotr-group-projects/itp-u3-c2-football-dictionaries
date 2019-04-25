from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_country_and_position(squads_list):
    squads_list = players_as_dictionaries(squads_list)
    players = {}
    for player in squads_list:
        country = player['country']
        position = player['position']
        players.setdefault(country,{})
        players[country].setdefault(position,[])
        players[country][position].append(player)
    return players
