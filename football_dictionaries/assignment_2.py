#from squads_data import SQUADS_DATA
#from pprint import pprint



def players_by_position(squads_list):
    player_position_dict = {}
    player_list = []
    
    for player1 in squads_list:
        player_dict = {
            'number': player1[0],
            'position': player1[1],
            'name': player1[2],
            'date_of_birth': player1[3],
            'caps': player1[4],
            'club': player1[5],
            'country': player1[6],
            'club_country': player1[7],
            'year': player1[8]
        }
        player_list.append(player_dict)
        
    for player2 in player_list:
        position = player2['position']
        player_position_dict.setdefault(position, [])
        player_position_dict[position].append(player2)
    return player_position_dict

#pprint(players_by_position(SQUADS_DATA))

