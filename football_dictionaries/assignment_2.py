from football_dictionaries.assignment_1 import transform_single_list_to_dic

def get_player_position(single_list):
    return single_list[1]

def players_by_position(squads_list):
    player_dic_by_positon = {}
    
    for player in squads_list:
        position = get_player_position(player)
        player_dic_by_positon.setdefault(position,[])
        player_dic = transform_single_list_to_dic(player)
        player_dic_by_positon[position].append(player_dic)
    
    return player_dic_by_positon
