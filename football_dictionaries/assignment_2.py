from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    position_list = {}
    
    players = players_as_dictionaries(squads_list)
    for player in players:
        position = player['position']
        position_list.setdefault(player['position'], [])
        position_list[position].append(player)
        
    
    return position_list