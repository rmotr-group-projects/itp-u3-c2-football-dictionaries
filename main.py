from football_dictionaries.squads_data import SQUADS_DATA
from football_dictionaries.assignment_1 import players_as_dictionaries
from pprint import pprint



def players_as_dictionaries(data):
    playerslist = []
    
    for player in data:
        playersdict = {
    'number': player[0],
    'position': player[1],
    'name': player[2],
    'date_of_birth': player[3],
    'caps': player[4],
    'club': player[5],
    'country': player[6],
    'club_country': player[7],
    'year': player[8],
}
        playerslist.append(playersdict)
    
    return playerslist
    
    


result = players_as_dictionaries(SQUADS_DATA)



pprint(result[1])
# print(len(result))


def players_by_position(data):
    position_player = {}
    playersdict = players_as_dictionaries(data)
    for player in playersdict:
        position = player['position']
        
        position_player.setdefault(position,[])
        position_player[position].append(player)
        
    return position_player

# result2 = players_by_position(SQUADS_DATA)
# goalkeepers = result2['GK']
# print(len(goalkeepers))

# print(result2)

# midfielders = result2['MF']
# assert len(midfielders) == 8
# assert midfielders[0] == {
#     'caps': '42',
#     'club': 'Royal Beerschot AC',
#     'club_country': 'Belgium',
#     'country': 'Belgium',
#     'date_of_birth': '(1900-10-26)26 October 1900 (aged 29)',
#     'name': 'Pierre Braine',
#     'number': '-',
#     'position': 'MF',
#     'year': '1930'
# }

# print(midfielders)

def players_by_country_and_position(data):
    results = {}
    
    playerdict = players_as_dictionaries(data)
    
    
    
    for player in playerdict:
        country = player['country']
        position = player['position']
        
        results.setdefault(country, {})
        results[country].setdefault(position, [])
        results[country][position].append(player)
        
    return results

# result = players_by_country_and_position(SQUADS_DATA)
# print(result)


