from football_dictionaries.assignment_1  import players_as_dictionaries


def players_by_position(SQUADS_DATA):
    players = {}
    multiple_positions = players_as_dictionaries(SQUADS_DATA)
    
    for player_position in multiple_positions:
        position = player_position["position"] 
        players.setdefault(position,[])
        players[position].append(player_position)
        
    return players

