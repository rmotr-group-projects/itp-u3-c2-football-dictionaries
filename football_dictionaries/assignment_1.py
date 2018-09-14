# def create_player_dictionary(player):
    
#     return {
#         'number': player[0],
#         'position': player[1],
#         'name': player[2],
#         'date_of_birth': player[3],
#         'caps': player[4],
#         'club': player[5],
#         'country': player[6],
#         'club_country': player[7],
#         'year': player[8],
#     }

def players_as_dictionaries(SQUADS_DATA):
    
    list_of_players = []
    
    for player in SQUADS_DATA:
        
        list_of_players.append({
            
            'number': player[0],
            'position': player[1],
            'name': player[2],
            'date_of_birth': player[3],
            'caps': player[4],
            'club': player[5],
            'country': player[6],
            'club_country': player[7],
            'year': player[8],
            
            })
    
    SQUADS_DATA = list_of_players
    
    return SQUADS_DATA


