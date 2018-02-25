from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_country_and_position(squads_list):
    
    country_dict = {}
    player_list = players_as_dictionaries(squads_list) #this is a list
    
    for player in player_list: #creates an empty dictionary for each footballing country  
        country_dict.setdefault(player['country'], {})
        country_dict[player['country']].setdefault(player['position'], []) #ex: {"Argentina: []"}
        country_dict[player['country']][player['position']].append(player) #adds player into the proper position in their country
    
    return country_dict
