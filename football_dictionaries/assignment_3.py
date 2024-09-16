from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_country_and_position(squads_list):
    players_by_country_pos={}
    players_list= players_as_dictionaries(squads_list)
    for player in players_list:
        country = player['country']
        position = player['position']
        players_by_country_pos.setdefault(country, {})
        players_by_country_pos[country].setdefault(position,[])
        players_by_country_pos[country][position].append(player)
    return players_by_country_pos
