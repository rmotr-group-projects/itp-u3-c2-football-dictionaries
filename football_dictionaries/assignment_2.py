from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    squads_list = players_as_dictionaries(squads_list)
    dict = {}
    for player in squads_list:
        position = player['position']
        dict.setdefault(position,[])
        dict[position].append(player)
    return dict

    
