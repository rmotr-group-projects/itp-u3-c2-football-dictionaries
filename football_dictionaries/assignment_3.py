from football_dictionaries.assignment_2 import players_by_position

def players_by_country_and_position(squads_list):
    players = players_by_position(squads_list)

    country_position_dict = {}
    for players_list in players.values():
        for player in players_list:
            country_position_dict.setdefault(player["country"], {})
            country_position_dict[player["country"]].setdefault(player["position"], [])
            country_position_dict[player["country"]][player["position"]].append(player)
    return country_position_dict
