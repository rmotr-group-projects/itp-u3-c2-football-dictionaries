from football_dictionaries.assignment_2 import players_by_position

def players_by_country_and_position(squads_list):
    pais_players = {}
    lista = {}
    pos_players = players_by_position(squads_list)
    for pos,players in pos_players.items(): 
        lista.setdefault(pos,[])
        for player in players:
            pais = player["country"]
            pais_players.setdefault(pais,lista)
            pais_players[pais][pos].append(player)
    print(pais_players)
    return pais_players
    
