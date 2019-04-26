def players_by_position(squads_list):
    position_dict = {}
    list_of_player_dict = []
    #group player into a list and bind it into a dict 
    for item in squads_list:
        player_dict = {
            'number': item[0],
            'position': item[1],
            'name': item[2],
            'date_of_birth':item[3],
            'caps':item[4],
            'club':item[5],
            'country':item[6],
            'club_country':item[7],
            'year':item[8]
            }
        list_of_player_dict.append(player_dict)
        position_dict.setdefault(item[1], []).append(player_dict)
    
    return position_dict

        #append list of player_dict into that empty list
        
'''        
# Please note we're returning a dictionary instead of a list
{
  "GK": [{..player1..}, {..player2..}],
  "DF": [{..player1..}, {..player2..}],
  "MF": [{..player1..}, {..player2..}],
  "FW": [{..player1..}, {..player2..}],
}
'''
