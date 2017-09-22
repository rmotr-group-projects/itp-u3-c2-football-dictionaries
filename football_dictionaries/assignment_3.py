#import function from assignment_2
from football_dictionaries.assignment_2 import players_by_position

def players_by_country_and_position(squads_list):
    
    # Creating a unique set of countries from the list    
    country_set=set()
    for players in squads_list:
        country_set.add(players[6])
        
    # Creating the dictionary of players
    country_roster_dictionary = {}
    
    for country in country_set:
        # This will be a list of players in a specific country
        country_player_list = []
        
        # Checks if the player if from the right country then adds him to the list
        for player in squads_list:
            if country in player:
                country_player_list.append(player)
        
        # adds the country as a key and the players organized by position just like assignment_2
        country_roster_dictionary[country] = players_by_position(country_player_list)
    
    return country_roster_dictionary