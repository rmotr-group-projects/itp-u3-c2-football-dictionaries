from .squads_data import SQUADS_DATA

# A template for how the dict should look

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

# Iterating to apply the template to every player

def players_as_dictionaries(squads_list):
    players_list = []
    for player in squads_list:
        player_as_dict = transform_list_player_to_dict(player)
        players_list.append(player_as_dict)
    return players_list

