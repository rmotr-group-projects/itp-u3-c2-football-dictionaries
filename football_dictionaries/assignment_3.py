from football_dictionaries.assignment_1 import players_as_dictionaries

#from pprint import pprint 

def players_by_country_and_position(squads_list):
    result = {}
    
    #importing dictionary from assignment_2
    player_dict = players_as_dictionaries(squads_list)
    
    for player in player_dict:
        country = player['country']  
        position = player['position']
        result.setdefault(country, {})
        result[country].setdefault(position,[])
        result[country][position].append(player)
        
    return result    


#from squads_data import SQUADS_DATA
#pprint(players_by_country_and_position(SQUADS_DATA))    
        


