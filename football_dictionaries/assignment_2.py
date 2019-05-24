from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    players_list= players_as_dictionaries(squads_list)
    players_by_pos_dict={}
    for player in players_list:       
        position=player['position']
        players_by_pos_dict.setdefault(position,[])
        players_by_pos_dict[position].append(player)
    return players_by_pos_dict
