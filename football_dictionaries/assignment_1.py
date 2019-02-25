def transform_single_list_to_dic(player_list):
    player_dic = {
        'caps': player_list[4],
        'club': player_list[5],
        'club_country': player_list[7],
        'country': player_list[6],
        'date_of_birth': player_list[3],
        'name': player_list[2],
        'number': player_list[0],
        'position': player_list[1],
        'year': player_list[8]
    }
    return player_dic 

def players_as_dictionaries(squads_list):
    list_of_player_dic =[]
    for player in squads_list:
        dic_player = transform_single_list_to_dic(player)
        list_of_player_dic.append(dic_player)
    return list_of_player_dic
    