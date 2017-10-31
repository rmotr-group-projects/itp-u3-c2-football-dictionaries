from .assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    squad = players_as_dictionaries(squads_list)
    players_by_position_dict = {}
    for player in squad:
        position = player['position']  #"GK" 
        players_by_position_dict.setdefault(position, []) #{GK: [{}]}
        players_by_position_dict[position].append(player)
    
    return players_by_position_dict
    
# {
#   "GK": [{..player1..}, {..player2..}],
#   "DF": [{..player1..}, {..player2..}],
#   "MF": [{..player1..}, {..player2..}],
#   "FW": [{..player1..}, {..player2..}],
# }