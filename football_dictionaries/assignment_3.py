from pprint import pprint


def players_by_country_and_position(squads_list):
    country_dict = {}
    list_of_player_dict = []
    #group player into a list and bind it into a dict 
    for item in squads_list:
        country = item[-3]
        position = item[1]
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
        country_dict.setdefault(country, {})
        country_dict[country].setdefault(position, [])
        country_dict[country][position].append(player_dict)

        #list_of_player_dict.append(player_dict)
        #position_dict.setdefault(item[1], []).append(player_dict)
    
    return country_dict


        

        
            
                




'''
{
  "Argentina": {
    "GK": [{..player1..}, {..player2..}],
    "DF": [{..player1..}, {..player2..}],
    "MF": [{..player1..}, {..player2..}],
    "FW": [{..player1..}, {..player2..}],
  },
  "Brazil": {
    "GK": [{..player1..}, {..player2..}],
    "DF": [{..player1..}, {..player2..}],
    "MF": [{..player1..}, {..player2..}],
    "FW": [{..player1..}, {..player2..}],
  }
}
'''