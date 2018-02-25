from squads_data import SQUADS_DATA

def list_to_dict(lista):
    d = {
    'caps': lista[4],
    'club': lista[5],
    'club_country': lista[6],
    'country': lista[7],
    'date_of_birth': lista[3],
    'name': lista[2],
    'number': lista[0],
    'position': lista[1],
    'year': lista[8]
    }
    return d
  
def players_as_dictionaries(squads_list):
    result = []
    for player_list in squads_list:
        player = list_to_dict(player_list)
        result.append(player)
    return result