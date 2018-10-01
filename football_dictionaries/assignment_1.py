def players_as_dictionaries(squads_list):
    
    players_as_dict = []
    
    for player in squads_list:
        
        player_dict = {
            'number': player[0],
            'position': player[1],
            'name': player[2],
            'date_of_birth': player[3],
            'caps': player[4],
            'club': player[5],
            'country': player[6],
            'club_country': player[7],
            'year': player[8],
            
        }
        
        players_as_dict.append(player_dict)
    return players_as_dict

        
        

'''
 [
    "1",                                     # Number
    "GK",                                    # Position
    "Juan Botasso",                          # Name
    "(1908-10-23)23 October 1908 (aged 21)", # Date of Birth
    "",                                      # Caps
    "Quilmes",                               # Club
    "Argentina",                             # Country (Players Country)
    "Argentina",                             # Club Country
    "1930"                                   # Year
  ],
'''
