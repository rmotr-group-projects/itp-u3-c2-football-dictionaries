from assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    
    # Unique names of all positions in list
    position_set = set()
    
    # This will contain the players organized by position
    
    position_dictionary = {}
    
    key_tuple = ('number', 'position', 'name', 'date_of_birth', 'caps', 'club', 'country', 'club_country', 'year')
    
    # Find an add all unique positions to position_set 
    for players in squads_list:
        position_set.add(players[1])
    
    # Go through positions that are in the list 
    for position in position_set:
        # Create a list that will be the value per position key
        ##position_dictionary[position] =[]
        position_list = []
        print(type(position_dictionary))
        # Go through players in the squads_list 
        for players in squads_list:
            
            # Check if the player position matches position for the list
            if position in players:
                
                # Add the player to the list in dictionary form similar to assignment 1 except this time as a dictionary
                position_list.append(players)
        position_dictionary[position] = players_as_dictionaries(position_list)
        
    return position_dictionary
  