#import pprint as pp
#from squads_data import SQUADS_DATA

def players_as_dictionaries(squads_list):
    result = []
    attributes = [
        'number', 
        'position', 
        'name', 
        'date_of_birth', 
        'caps', 
        'club', 
        'country', 
        'club_country', 
        'year'
    ]
    
    for player in squads_list:
        player_dict = {}
        for i in range(len(player)):
            player_dict[attributes[i]] = player[i]
        result.append((player_dict))
    return result
        
#pp.pprint(players_as_dictionaries(SQUADS_DATA))