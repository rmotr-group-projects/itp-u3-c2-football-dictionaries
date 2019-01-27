from football_dictionaries.assignment_1 import players_as_dictionaries

#from pprint import pprint 

def players_by_position(squads_list):
    player_dict = {}
    
    #importing dictionary from assignment_1
    player_list = players_as_dictionaries(squads_list)
    
    for player in player_list:
        position = player['position']
# setting default as [] if position isn't already there
        player_dict.setdefault(position, [])
        player_dict[position].append(player)
        
    return player_dict    


#from squads_data import SQUADS_DATA
#pprint(players_by_position(SQUADS_DATA))    
        
