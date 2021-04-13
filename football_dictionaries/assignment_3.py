#from squads_data import SQUADS_DATA
#from pprint import pprint

def players_by_country_and_position(squads_list):
    player_list = []    
    country_dict = {}
    COUNTRY_LIST = ['Argentina', 'Belgium', 'Brazil', 'South Korea']
    
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
    
    for key in COUNTRY_LIST:
        player_position_dict = {}
        for player2 in player_list:
            country = player2['country']
            country_dict.setdefault(country, {})
            if key == country:
                position = player2['position']
                player_position_dict.setdefault(position,[])
                player_position_dict[position].append(player2)
                country_dict[key] = player_position_dict

    return country_dict


#pprint(players_by_country_and_position(SQUADS_DATA))