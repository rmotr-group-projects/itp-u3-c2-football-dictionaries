import football_dictionaries.assignment_1 as asd

def players_by_country_and_position(squads_list):
    list_of_players = asd.players_as_dictionaries(squads_list)
    country_dict = {}
    for player in list_of_players:
        country_dict.setdefault(player['country'],{})
        country_dict[player['country']].setdefault(player['position'],[])
        country_dict[player['country']][player['position']].append(player)
    return country_dict
    