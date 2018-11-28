from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    squads_dict = players_as_dictionaries(squads_list)
    player_by_post = {}
    for squad in squads_dict:
        position = squad['position']
        player_by_post.setdefault(position, [])
        player_by_post[position].append(squad)
    return player_by_post