# Assignment 1
from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_country_and_position(SQUADS_DATA):
    players_by_country = {}
    players_by_position = players_as_dictionaries(SQUADS_DATA)
    
    for player in players_by_position: # loop through each player dictionary
        
        country_val = player["country"] # country value
        
        position_val = player["position"] # play position value
        
        players_by_country.setdefault(country_val, {}) # country key is root
        
        players_by_country[country_val].setdefault(position_val,[]) # position val 
                                                                    #is child list
        
        players_by_country[country_val][position_val].append(player) # append player to
                                                                     # player list and each                                                                                      # player list to country
        
        
        
        
        
        
    return players_by_country
        
        
        
        
        