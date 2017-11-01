from squads_data import SQUADS_DATA

def list_to_dict(lista):
    d = {
    'caps': lista[4],
    'club': lista[5],
    'club_country': lista[7],
    'country': lista[6],
    'date_of_birth': lista[3],
    'name': lista[2],
    'number': lista[0],
    'position': lista[1],
    'year': lista[8]
    }
    return d
    
def players_by_country_and_position(squads_list):
    result = {}

    for player_list in squads_list:
        player = list_to_dict(player_list)
        position = player['position']
        country = player['country']
        
        if country not in result:
            result[country] = {}
        
        if position not in result[country]:
            result[country][position] = []
        result[country][position].append(player)
    return result

