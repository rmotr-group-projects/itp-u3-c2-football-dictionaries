from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_country_and_position(squads_list):
    squad_dict = players_as_dictionaries(squads_list)
    country_dict = {}
    for player in squad_dict():
        country = player.get('country')
        position = player.get('position')
        country_dict.setdefault(country, {})
        country_dict[country].setdefault(position, [])
        country_dict[country][position].append(player)

    return country_dict
