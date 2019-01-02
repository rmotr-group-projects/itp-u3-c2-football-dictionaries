#from squads_data import SQUADS_DATA

def players_by_position(squads_list):
    #sort into dictionary by position
    
    position_dictionary = {}
    
    #squads_list is a LIST OF LISTS
    # FILL IN THE DICTIONARY WITH POSITIONS FIRST
    for one_list in squads_list:
        #make an empty dictionary of the positions (second index in each list)
        position_dictionary.setdefault(one_list[1], [])
    print(position_dictionary)
    
    # Now use the dictionary keys to find the players and add them (append that list)
    list_categories = ['number','position','name','date_of_birth','caps','club','country','club_country','year']
    
        # go through player by player
    for one_player in squads_list:
        print("one player: ", one_player[1])
        
        #zip two lists together (combine at same index)
        single_player_dictionary = dict(zip(list_categories,one_player))

        # add each player to the correct dictionary key
        # key from each player...
        position_dictionary[single_player_dictionary['position']].append(single_player_dictionary)
        
        #print(position_dictionary)
        #print(single_player_dictionary)
        
    return position_dictionary

'''
# Please note we're returning a dictionary instead of a list
{
  "GK": [{..player1..}, {..player2..}],
  "DF": [{..player1..}, {..player2..}],
  "MF": [{..player1..}, {..player2..}],
  "FW": [{..player1..}, {..player2..}],
}
'''

# The method setdefault() is similar to get(), but will set dict[key]=default if key is not already in dict.

#print(players_by_position(SQUADS_DATA))