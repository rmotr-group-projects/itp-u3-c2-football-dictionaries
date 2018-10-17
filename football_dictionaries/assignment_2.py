# Assignment 1 code
def transform_list_player_to_dict(player_as_list):
    template = {
        'number': player_as_list[0],
        'position': player_as_list[1],
        'name': player_as_list[2],
        'date_of_birth': player_as_list[3],
        'caps': player_as_list[4],
        'club': player_as_list[5],
        'country': player_as_list[6],
        'club_country': player_as_list[7],
        'year': player_as_list[8],
    }
    return template

# Grouping players by position
def players_by_position(squads_list):
    players = {
        'GK': [],
        'MF': [],
        'FW': []
    }
    for player_as_list in squads_list:
        player = transform_list_player_to_dict(player_as_list)
        position = player['position']

        players[position].append(player)

    return players
