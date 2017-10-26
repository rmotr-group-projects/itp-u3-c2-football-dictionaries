from pprint import pprint
#from squads_data import SQUADS_DATA

def players_as_dictionaries(squads_list):
    list_key = ['number', 'position', 'name', 'date_of_birth', 'caps', 'club', 'country', 'club_country', 'year']
    results = []
    for item in squads_list:
        results.append(dict(zip(list_key,item)))
    return results

    
#pprint(players_as_dictionaries(SQUADS_DATA))