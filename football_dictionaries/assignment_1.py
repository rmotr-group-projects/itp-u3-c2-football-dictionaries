from .squads_data import SQUADS_DATA
from pprint import pprint

def players_as_dictionaries(squads_list):
    ''' Turn list of players information into dictionaries. '''
    team_list = []
    for player in squads_list:
        players_dict = {
            'number': player[0],
            'position': player[1],
            'name': player[2],
            'date_of_birth': player[3],
            'caps': player[4],
            'club': player[5],
            'country': player[6],
            'club_country': player[7],
            'year': player[8],
        }
        team_list.append(players_dict)
    return team_list

pprint(players_as_dictionaries(SQUADS_DATA))

'''
[
    {
        'number': ...,
        'position': ...,
        'name': ...,
        'date_of_birth': ...,
        'caps': ...,
        'club': ...,
        'country': ...,
        'club_country': ...,
        'year': ...,
    }
]
'''