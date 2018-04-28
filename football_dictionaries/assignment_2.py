#import pprint as pp
#from squads_data import SQUADS_DATA

def players_by_position(squads_list):
    players = []
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
        players.append((player_dict))
    
    positions = {}
    for player in players:
        positions.setdefault(player['position'], [])
        positions[player['position']].append(player)
    return positions
    
#pp.pprint(players_by_position(SQUADS_DATA))
