from .assignment_1 import players_as_dictionaries
from pprint import pprint
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
def players_by_country_and_position(squads_list):
    countries = {}
    players = players_as_dictionaries(squads_list)
    
    for player in players:
        position = player['position']
        country = player['country']
        
       
        
        countries.setdefault(country, {})
        countries[country].setdefault(position, [])
        countries[country][position].append(player)
        
    #return final_dictionary_position
    #pprint(final_dictionary_country)
    print(countries.keys())
    return countries

