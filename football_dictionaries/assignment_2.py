from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    player_list = players_as_dictionaries(squads_list)
    
    

    positions = [] #unique list of positions
    list_by_position = [[],[],[]] #list of players by position
    number_of_players = len(player_list)
#this loop creates a unique list of keys
    for position in range(number_of_players):
        if player_list[position]['position'] not in positions:
            positions.append(player_list[position]['position'])     
#this loop groups my players into three different lists based on position. let's try to make this a nested loop, creating a list of three lists.
    for position_key in range(len(positions)):
        for player in range(number_of_players):
            if player_list[player]['position'] == positions[position_key]:
                list_by_position[position_key].append(player_list[player])    
    list_of_grouped_players = dict(zip(positions, list_by_position))
    return list_of_grouped_players
