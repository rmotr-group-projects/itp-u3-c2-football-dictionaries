



 
'''
player_list = ['number','position','name','date_of_birth','caps','club', 'country', 'club_country', 'year']
players = [
 
    "1",                                     # Number
    "GK",                                    # Position
    "Juan Botasso",                          # Name
    "(1908-10-23)23 October 1908 (aged 21)", # Date of Birth
    "",                                      # Caps
    "Quilmes",                               # Club
    "Argentina",                             # Country (Players Country)
    "Argentina",                             # Club Country
    "1930"                                   # Year
  ]
  
 
 
 #option 1
player_dict = {
        'number': players[0],
        'position': players[1],
        'name': players[2],
        'Date_of_birth': players[3],
        'Caps': players[4],
        'Club': players[5],
        'Country (Players Country)': players[6],
        'Club Country': players[7],
        'Year': players[8]
        }

pprint(player_dict)

#option 2
def player_dict_1(key_list, value_list):
    return { key_list[i] : players[i] for i in range(len(player_list)) }
pprint(player_dict_1(player_list, players))
  
    
#option 3
player_dict_2 = dict((key, value) for (key, value) in zip(player_list, players))   
pprint (player_dict_2) 
'''


      
def players_as_dictionaries(squads_list):
    player_list = ['number','position','name','date_of_birth','caps','club', 'country', 'club_country', 'year']
    final_player_list = []
    for player_data in squads_list:   #comment here
        player_dict = {}
        for key, value in zip(player_list, player_data):  #comment here
            player_dict[key] = value
        final_player_list.append(player_dict)
        
    return final_player_list