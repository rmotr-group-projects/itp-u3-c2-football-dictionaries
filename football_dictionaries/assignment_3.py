from football_dictionaries.assignment_2 import players_by_position

def players_by_country_and_position(squads_list):
    pais_players = {}
    posiciones_dic = {}
    pos_players = players_by_position(squads_list)
    for pos,players in pos_players.items(): 
        for player in players:
            pais = player["country"]
            pais_players.setdefault(pais,{})
            for key_pais, dic_pos in pais_players.items():
                if pais == key_pais:
                    pais_players[pais].setdefault(pos,[])
                    pais_players[pais][pos].append(player)        
    return pais_players
    
