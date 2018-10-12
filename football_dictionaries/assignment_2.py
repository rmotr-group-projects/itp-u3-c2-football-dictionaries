from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    positions_list = {}

    players = players_as_dictionaries(squads_list)


    for player in players:
        position = player['position']
        positions_list.setdefault(player['position'], [])
        positions_list[position].append(player)

    return positions_list