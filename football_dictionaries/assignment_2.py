from football_dictionaries.assignment_1 import players_as_dictionaries



def players_by_position(squads_list):
    player_list = players_as_dictionaries(squads_list)
    players_position = {}
    for players in player_list:
        position = players['position']
        players_position.setdefault(position, [])
        players_position[position].append(players)
    return players_position
