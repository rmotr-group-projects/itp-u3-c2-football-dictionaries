# Assignment 1
from football_dictionaries.assignment_1 import players_as_dictionaries
# Assignment 2
from football_dictionaries.assignment_2 import players_by_position

def players_by_country_and_position(squads_list):
    players_dict = players_as_dictionaries(squads_list)
    players_by_country={}
    player_by_country_and_position={}
    for player in players_dict:
        players_by_country.setdefault(player['country'],[])
        players_by_country[player['country']].append(player)
    for country,country_list in players_by_country.items():
        player_by_country_and_position.setdefault(country,{})
        for player in country_list:
            player_by_country_and_position[country].setdefault(player['position'],[])
            player_by_country_and_position[country][player['position']].append(player)
    return player_by_country_and_position    
        
        
