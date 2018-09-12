def transform_list(player_as_list):
    player_dict = {
        'caps': player_as_list[4],
        'club': player_as_list[5],
        'club_country': player_as_list[7],
        'country': player_as_list[6],
        'date_of_birth': player_as_list[3],
        'name': player_as_list[2],
        'number': player_as_list[0],
        'position': player_as_list[1],
        'year': player_as_list[8]
    }
    return player_dict

def players_by_position(squads_list):
    players = {
        'GK':[],
        'MF':[],
        'FW':[]
        
    }
    
    for player_as_list in squads_list:
        player = transform_list(player_as_list)
        position = player['position']
        
        players[position].append(player)
        
    return players 
    
def players_by_country_and_position(squads_list):
    countries ={}
    players =None
    
    for player_as_list in squads_list:
        player = transform_list(player_as_list)
        position = player['position']
        country = player['country']
        
        countries.setdefault(country,{})
        countries[country].setdefault(position,[])
        countries[country][position].append(player)
    return countries    
"""
     convert players to dicts
     for player
        check if players country is in dict
        check if players position is in country dict
        add player
        
    get list of players
    sort players by country
    sort players by position within country
     """
        
        
    
"""   
country.setdefault("Canada", {})
country['Canada'].setdefault(pos, [])
    d = {}
if 'my_key' not in d:
    d['my_key'] = "my default"
d.setdefault("my_key", "my default")
"""