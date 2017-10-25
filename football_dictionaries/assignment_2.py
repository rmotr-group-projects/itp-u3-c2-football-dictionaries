from assignment_1 import players_as_dictionaries

def players_by_position(squad_list):
    player_list = players_as_dictionaries(squad_list)
    new_player_dictionary = {}
    for player in player_list:
        if player['position'] not in new_player_dictionary:
            new_player_dictionary[player['position']] = []
        new_player_dictionary[player['position']].append(player)
    return new_player_dictionary
        

