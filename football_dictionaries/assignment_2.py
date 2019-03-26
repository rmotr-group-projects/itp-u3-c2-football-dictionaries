from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    pos_players = {}
    list_dic_players = players_as_dictionaries(squads_list)
    for player in list_dic_players:
        position = player["position"]
        pos_players.setdefault(position,[])
        pos_players[position].append(player)
    return pos_players
