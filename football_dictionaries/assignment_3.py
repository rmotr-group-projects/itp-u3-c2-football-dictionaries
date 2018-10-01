'''
This section is code for assignment_1
'''

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
#-------------------------------------------------------------------------------
'''
This section is code for assignment_2
'''
def players_by_position(squads_list):
    
    '''so we want a dictionary and each key in the dictionary
    will be a list of player dictionaries
    '''
    
    # This will give me a list with each player as a dictionary
    
    players_as_dict = players_as_dictionaries(squads_list)
    
    dict_of_positions = {}
    
    for player in players_as_dict:
        
        dict_of_positions.setdefault(player['position'], [])
        
        dict_of_positions[player['position']].append(player)
        
    return dict_of_positions

'''
This section is code for assignment_3
'''

#-------------------------------------------------------------------------------
'''
For this function we need a dictionary of countries. Each country will contain
a dictionary of positions. Each position will have a list which contains
every player playing in that position as a dictionary.
'''


def players_by_country_and_position(squads_list):



  dict_of_country = {}
  players_as_dict = players_as_dictionaries(squads_list)
  dict_of_positions = players_by_position(squads_list)
    
  
    
  for player_ctry in players_as_dict:
    
    #getting dictionary of countries with empty dictionaries as values
    dict_of_country.setdefault(player_ctry['country'], {}) 
    
    #defining the inner dictionary for keys in each country dictionary
    inner_dict_of_pos = {}
    
    for position in dict_of_positions.keys():
      
      # creating inner dictionaries for positions and assigning empty lists as values to store player dictionaries later
      inner_dict_of_pos.setdefault(position, [])
      
      #This for loop loops through each player and checks if their country and position matches with the outer-most country and position keys.
      #If so, that player is added to the position-key value
      
      for player in players_as_dict:
        
        if (player['country'] == player_ctry['country']) and (player['position'] == position):
          
          inner_dict_of_pos[position].append(player)
      
      #If-statement to delete a position in a country if it contains no player (empty)
      if inner_dict_of_pos[position] == []:
        del inner_dict_of_pos[position]
    
    dict_of_country[player_ctry['country']].update(inner_dict_of_pos)
    
 
        
  return dict_of_country