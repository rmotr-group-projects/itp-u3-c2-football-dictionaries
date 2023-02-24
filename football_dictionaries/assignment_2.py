def players_by_position(squads_list):
    final_list = []
    for item in squads_list:
        final_dict = {'number': item[0],
        'position': item[1],
        'name': item[2],
        'date_of_birth': item[3],
        'caps': item[4],
        'club': item[5],
        'country': item[6],
        'club_country': item[7],
        'year': item[8]}
        final_list.append(final_dict)
        
    position_dict = {
        'GK': [],
#         'DF': [],
        'MF': [],
        'FW': []
    }
    for player in final_list:
        if player['position'] == "GK":
            position_dict["GK"].append(player)
#         elif player['position'] == "DF":
#             position_dict["DF"].append(player)
        elif player['position'] == "MF":
            position_dict["MF"].append(player)
        elif player['position'] == "FW":
            position_dict["FW"].append(player)
    return position_dict