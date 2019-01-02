from football_dictionaries.assignment_1 import * #import all of the functions (yes just one)

#import pprint

# FIRST GROUP THEM BY COUNTRY, then by position

def players_by_country_and_position(squads_list):
    # get the list of player dictionaries
    list_of_squad_dictionaries = players_as_dictionaries(squads_list)

    position_dictionary = {}
    
    # FILL IN THE DICTIONARY WITH COUNTRIES FIRST...
    for one_list in squads_list:
        #print("one_list[6]",one_list[6]) #COUNTRY
        #print("one_list[1]",one_list[1]) #POSITION
        
        # default value is an empty dictionary (testing this default dictionaries must be set first)
        position_dictionary.setdefault(one_list[6], {})

        position_dictionary[one_list[6]].update({one_list[1]:[]})
        
        #print("DEBUG: country:", position_dictionary)
    
    #print("DEBUG: position_dictionary",position_dictionary)
    
    #put the players in the position_dictionary
    #traverse list of players
    #print("AMOUNT OF PLAYERS", len(list_of_squad_dictionaries))
    
    for player in list_of_squad_dictionaries:
        #print("player", player)
        #position_dictionary[player['country']][player['position']] = player
        position_dictionary[player['country']][player['position']].append(player)
    
    #pprint.pprint(position_dictionary)
    
    return position_dictionary

# Is there a better way to do this?

'''
{
  "Argentina": {
    "GK": [{..player1..}, {..player2..}],
    "DF": [{..player1..}, {..player2..}],
    "MF": [{..player1..}, {..player2..}],
    "FW": [{..player1..}, {..player2..}],
  },
  "Brazil": {
    "GK": [{..player1..}, {..player2..}],
    "DF": [{..player1..}, {..player2..}],
    "MF": [{..player1..}, {..player2..}],
    "FW": [{..player1..}, {..player2..}],
  }
}
'''

# The method setdefault() is similar to get(), but will set dict[key]=default if key is not already in dict.

#print(players_by_country_and_position(SQUADS_DATA))
#players_by_country_and_position(SQUADS_DATA)