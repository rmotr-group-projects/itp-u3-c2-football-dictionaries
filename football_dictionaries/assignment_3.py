from football_dictionaries.assignment_1 import players_as_dictionaries
from football_dictionaries.squads_data import SQUADS_DATA
from pprint import pprint

#since we're importing from #1, the code in #2 won't apply and will need to be reconstructed

def players_by_country_and_position(squads_list):
    player_countries = {} #expected result is a dict:key(being another dict with the 4 roles)
    player_dictionary = players_as_dictionaries(squads_list) # variable has been set as function call
    
    for player in player_dictionary: # looping over each player
        player_countries.setdefault(player['country'],{}) #set default key value, empty dictionary
        player_countries[player['country']].setdefault(player['position'], [])# update players by country key
        player_countries[player['country']][player['position']].append(player)
        
    return player_countries

pprint(players_by_country_and_position(SQUADS_DATA))

#remove england germany, italy

# To do
# recreate the code from #2 and implement here to pass test

#Reason for failing
# Assert Error, because the #2 results are not imported, they need to be recreated.
        
# only one level higher, set default country and empty dictionary