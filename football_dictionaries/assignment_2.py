from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    position_dict = {}  #dictionary with positions as keys and players that play those positions as values
    players_list = players_as_dictionaries(squads_list)  #using players_as_dictionaries(SQUADS_DATA) to access players dictionary
    for player in players_list: 
        position_dict.setdefault(player['position'], [])  #initializing the players position with an empty list within position_dict if it doesnt exist
        position_dict[player['position']].append(player)  #appending player to the player's respective position key within position_dict
    return position_dict

