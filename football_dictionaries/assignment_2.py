from .assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    '''Input a list of lists where each internal list represents a player
        Use method from assignment_1 to convert to a list of dictionaries where each dictionary represents a player
        Output a dictionary of player positions (keys) and players (values)'''
    squads_dict = players_as_dictionaries(squads_list)
    dict_by_position = {}
    for player in squads_dict:
        position = player['position']
        dict_by_position.setdefault(position,[])
        dict_by_position[position].append(player)
    return dict_by_position