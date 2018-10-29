from pprint import pprint 

from football_dictionaries.squads_data import SQUADS_DATA

def player_list_to_dict(list_of_player):
    player_dictionaries = {
        'caps': list_of_player[4],
        'club': list_of_player[5],
        'club_country': list_of_player[7],
        'country': list_of_player[6],
        'date_of_birth': list_of_player[3],
        'name': list_of_player[2],
        'number': list_of_player[0],
        'position': list_of_player[1],
        'year': list_of_player[8]
    }
    return player_dictionaries

def players_by_position(squads_list):
    players = {
        "GK": [],
        "MF": [],
        "FW": []
    }
    for player_list in squads_list:
        player = player_list_to_dict(player_list)
        position = player['position']
        
          
        players[position].append(player)
      
    
    return players

pprint(players_by_position(SQUADS_DATA))