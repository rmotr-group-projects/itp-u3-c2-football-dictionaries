#import function from assignment_2
from assignment_2 import players_by_position

def players_by_country_and_position(squads_list):
    
    # Creating a unique set of countries from the list    
    country_set=set()
    for players in squads_list:
        country_set.add(players[6])
        
    country_roster_dictionary = {}

    #for country in country_set:
    #    country_player_list =[]
    #    for player in squads_list:
    #        if country in player:
    #            country_player_list.append(player)
    #    country_roster_dictionary[country] = players_by_position(country_player_list)
    
    pass    
    return country_roster_dictionary