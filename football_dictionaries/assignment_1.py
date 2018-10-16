def players_as_dictionaries(squads_list):
    result = []
    
    for player in squads_list:
        player_dict = {
            'caps': player[4],
            'club': player[5],
            'club_country': player[7],
            'country': player[6],
            'date_of_birth': player[3],
            'name': player[2],
            'number': player[0],
            'position': player[1],
            'year': player[8]
        }
        
        result.append(player_dict)
    
    return result
    
# # Data
# import pprint
# from squads_data import SQUADS_DATA

# pprint.pprint(players_as_dictionaries(SQUADS_DATA))