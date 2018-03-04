from squads_data import SQUADS_DATA

# Transform 1 record of list to dictionary function
def transform_dict(player):
   # dictionary that assign keys to position in list from parameter
    result = {'caps': player[4],
        'club': player[5],
        'club_country': player[7],
        'country': player[6],
        'date_of_birth': player[3],
        'name': player[2],
        'number': player[0],
        'position': player[1],
        'year': player[8]
    }
    
    return result


def players_as_dictionaries(squad_list):
    # Empty list to hold all dictionaries
    player_list = []
    
    # Loop through parameter list
    for player in squad_list:
        # Pass the current position from list into function to transfer to dict
        player = transform_dict(player)
        # Append entire dict to list
        player_list.append(player)
    
    return player_list


#print(players_as_dictionaries(SQUADS_DATA))