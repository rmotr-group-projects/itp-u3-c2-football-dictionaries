from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    squad_dict = players_as_dictionaries(squads_list)
    pos_dict = {}
    for player in squad_dict:
        pos = player.get('position')
        pos_dict.setdefault(pos, [])
        pos_dict[pos].append(player)
    return pos_dict
