from football_dictionaries.assignment_1 import players_as_dictionaries
from football_dictionaries.assignment_2 import players_by_position
'''
Dict > Dict > List > Dict
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
    ppositions = players_as_dictionaries(squads_list)
    player_country = {}
    for player in ppositions:
        country = player['country']
        position = player['position']
        player_country.setdefault(country,{})
        player_country[country].setdefault(position,[])
        player_country[country][position].append(player)
        
    return player_country
