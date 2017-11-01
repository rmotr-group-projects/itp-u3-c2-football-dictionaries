from football_dictionaries.assignment_1 import players_as_dictionaries


def players_by_position(squads_list):
    formatted_list = players_as_dictionaries(squads_list)
    positions_list = {}
    
    # gets positions from all the players
    for player in formatted_list:
        position = player.get('position')
        # adds a field position
        positions_list.setdefault(position, [])
        # adds the player to their respective list
        # by position
        positions_list[position].append(player)

    return positions_list
 