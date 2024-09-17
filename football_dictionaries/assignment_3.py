from football_dictionaries.assignment_1 import players_as_dictionaries


def players_by_country_and_position(squads_list):
    country_dict = {}
    for player in players_as_dictionaries(squads_list):
        if player['country'] not in country_dict.keys():
            country_dict.setdefault(player['country'], {})
        if player["position"] not in country_dict[player['country']]:
            country_dict[player['country']].setdefault(player['position'], [player])
        else:
            country_dict[player['country']][player["position"]].append(player)
    return country_dict
