from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_country_and_position(squads_list):
    player_list = players_as_dictionaries(squads_list)
    players_country_position = {}
    
    country_set = set()
    for player in player_list:
        country = player['country']
        country_set.add(country)
    
    player_country = dict.fromkeys(country_set, {})
    print(player_country)
        
        
    for country in player_country:
        player_position = {}
        for player in player_list:
            position = player['position']
            if player['country'] == country:
                player_position.setdefault(position, [])
                player_position[position].append(player)
        player_country[country] = player_position
    
    print(player_country)
    return player_country

        
    
            
            

            
            
