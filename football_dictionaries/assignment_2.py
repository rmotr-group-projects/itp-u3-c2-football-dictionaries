from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    squads_list = players_as_dictionaries(squads_list)  # must format list (again) from data
    positions = {}  # declare dict for storage 
    
    for player in squads_list:
        position_key = player['position']       # find the player's postn in list (eg GK)
        positions.setdefault(position_key, [])  # set the key to None or error
        positions[position_key].append(player)  # append entire player by his position
    
    return positions

