from football_dictionaries.squads_data import SQUADS_DATA


def player_list_to_dict(player_list):
    return{'number': player_list[0],
           'position': player_list[1],
           'name': player_list[2],
           'date_of_birth': player_list[3],
           'caps': player_list[4],
           'club': player_list[5],
           'country': player_list[6],
           'club_country': player_list[7],
           'year': player_list[8]
           }


def players_by_country_and_position(squads_list):
    result = {}
    for player_list in squads_list:
        player = player_list_to_dict(player_list)
        country = player['country']
        position = player['position']
        if country not in result:
            result[country] = {}
        if position not in result[country]:
            result[country][position] = []
        result[country][position].append(player)
    return result