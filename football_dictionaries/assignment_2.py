from football_dictionaries.assignment_1 import players_as_dictionaries


def players_by_position(squads_list):
    positions = []
    positions_list = {}
    formatted_list = players_as_dictionaries(squads_list)

    # gets positions from all the players
    for player in formatted_list:
        player_position = player.get('position')
        positions.append(player_position)
        # sets default positions for positions list
        for position in positions:
            positions_list.setdefault(position, [])
        # if position matches, add the player to that group            
        for position in positions_list:
            if player_position == position:
                positions_list[player_position].append(player)

    return positions_list
