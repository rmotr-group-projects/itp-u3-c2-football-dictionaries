def players_as_dictionaries(squads_list):
    squad_dictionary = []
    for player in squads_list:
        player_dictionary = {
            'number': player[0],
            'position' : player[1],
            'name': player[2],
            'date_of_birth': player[3],
            'caps': player[4],
            'club': player[5],
            'country': player[6],
            'club_country': player[7],
            'year': player[8],
        }
        squad_dictionary.append(player_dictionary)
    return squad_dictionary

def players_by_country_and_position(squads_list):
    player_country = {
        
    }
    for player in players_as_dictionaries(squads_list):
        country = player["country"]
        position = player["position"]
        if country not in player_country:
            player_country[country] = {}
        if position not in player_country[country]:
            player_country[country][position] = []
        player_country[country][position].append(player)
    return player_country
  