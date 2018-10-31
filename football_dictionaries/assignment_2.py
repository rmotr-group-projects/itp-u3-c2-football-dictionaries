from assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    data = players_as_dictionaries(squads_list)
    positions = {}
    for player in data:
        position = player['position']
        if position not in positions:
            positions[position] = []
        positions[position].append(player)
    return positions
