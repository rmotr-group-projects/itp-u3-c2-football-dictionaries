from .assignment_1 import transform_list_player_to_dictionary
def players_by_country_and_position(squads_list):
    players={}
    
    for player_as_list in squads_list:
        player=transform_list_player_to_dictionary(player_as_list)
        country=player['country']
        players.setdefault(country,{})
        position=player['position']
        players[country].setdefault(position,[])
        players[country][position].append(player)
    return players
        
    
    
        
        
        
        


        
        

        
