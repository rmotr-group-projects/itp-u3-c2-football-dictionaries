from .assignment_1 import players_as_dictionaries
from .squads_data import SQUADS_DATA

def players_by_position(squads_list):
    # create a dictionary by position. Append each player's dictionary on to a list
    profiles = players_as_dictionaries(squads_list)
    positions = {}

    for player in profiles:
        positions.setdefault(player['position'], []).append(player)
    
    return positions

    """
    # Please note we're returning a dictionary instead of a list
    {
      "GK": [{..player1..}, {..player2..}],
      "DF": [{..player1..}, {..player2..}],
      "MF": [{..player1..}, {..player2..}],
      "FW": [{..player1..}, {..player2..}],
    }
    
    """