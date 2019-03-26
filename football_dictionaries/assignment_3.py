from football_dictionaries.assignment_2 import players_by_position

def players_by_country_and_position(squads_list):
    pais_players = {}
    lista ={}
    pos_players = players_by_position(squads_list)
    for pos,players in pos_players.items(): 
        for player in players:
            pais = player["country"]
            pais_players.setdefault(pais,{})
    for p in list(pais_players.keys()):
        for pos,players in pos_players.items(): 
            for player in players:
                if p == player["country"]:
                    pais_players[p]=lista.setdefault(pos,[])
                    pais_players[p]= lista 
                    lista[pos].append(player)
    return pais_players
    
