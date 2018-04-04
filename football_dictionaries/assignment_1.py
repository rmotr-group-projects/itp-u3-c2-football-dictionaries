from football_dictionaries.squads_data import SQUADS_DATA

def players_as_dictionaries(squads_list):
    player_list_of_dict = []  #list with individual player dictionaries
    for player in squads_list:  #iterate over each player's list 'SQUADS_DATA' from squads_data.py
        player_list_of_dict.append({  #append each individual 'player' values, assinging them to respective keys
            'number': player[0], 
            'position': player[1],
            'name': player[2], 
            'date_of_birth': player[3],
            'caps': player[4],
            'club': player[5],
            'country': player[6],
            'club_country': player[7],
            'year': player[8]
            })
    return player_list_of_dict
     

    