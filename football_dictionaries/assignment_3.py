#import pprint as pp
#from squads_data import SQUADS_DATA

def players_by_country_and_position(squads_list):
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
    
    countries = {}
    for player in players:
        countries.setdefault(player['country'],{})
        countries[player['country']].setdefault(player['position'], [])
        countries[player['country']][player['position']].append(player)
    return countries
    
#pp.pprint(players_by_country_and_position(SQUADS_DATA))

