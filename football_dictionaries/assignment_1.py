'''
#from football_dictionaries.squads_data import SQUADS_DATA
import squads_data
    
player_list = [
    "1",
    "GK",
    "Juan Botasso",
    "(1908-10-23)23 October 1908 (aged 21)",
    "",
    "Quilmes",
    "Argentina",
    "Argentina",
    "1930"
    ]
player_dict = None
    
def change_list_to_dict(player_list):
    player_dict = {
        'number': player_list[0],
        'position': player_list[1],
        'name': player_list[2],
        'date_of_birth': player_list[3],
        'caps': player_list[4],
        'club': player_list[5],
        'club_country': player_list[6],
        'country': player_list[7],
        'year': player_list[8]
    }
    return player_dict
    
assert player_dict == {
            'caps': '',
            'club': 'Quilmes',
            'club_country': 'Argentina',
            'country': 'Argentina',
            'date_of_birth': '(1908-10-23)23 October 1908 (aged 21)',
            'name': 'Juan Botasso',
            'number': '1',
            'position': 'GK',
            'year': '1930'
        }
print("It worked!")

def players_as_dictionaries(squads_list):
    player_list = []
    for player in squads_list:
        player_dict = change_list_to_player(player)
        player_list.append(player_dict)
    return player_list
'''




from .squads_data import SQUADS_DATA


def players_as_dictionaries(squads_list):
    player_list = [
    'number',
    'position',
    'name',
    'date_of_birth',
    'caps',
    'club',
    'country',
    'club_country',
    'year']
    final_list = []
    for player in squads_list:
        final_list.append(dict(zip(player_list, player)))
    return final_list
    
print(players_as_dictionaries(SQUADS_DATA)[0])
