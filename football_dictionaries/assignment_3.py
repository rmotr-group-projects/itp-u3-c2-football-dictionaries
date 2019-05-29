def players_by_country_and_position(squads_list):
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
    
    final_country = {}
    for player in final_list:
        player_country = player['country']
        player_position = player['position']
        final_country.setdefault(player_country, {})
        final_country[player_country].setdefault(player_position, []).append(player)
    return final_country
        

        
        
#         {
#   "Argentina": {
#     "GK": [{..player1..}, {..player2..}],
#     "DF": [{..player1..}, {..player2..}],
#     "MF": [{..player1..}, {..player2..}],
#     "FW": [{..player1..}, {..player2..}],
#   },
#   "Brazil": {
#     "GK": [{..player1..}, {..player2..}],
#     "DF": [{..player1..}, {..player2..}],
#     "MF": [{..player1..}, {..player2..}],
#     "FW": [{..player1..}, {..player2..}],
#   }
# }