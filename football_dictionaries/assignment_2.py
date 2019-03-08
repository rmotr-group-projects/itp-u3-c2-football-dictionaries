from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_position(squads_list):    
    positions = {}
    position = ''
    for player in players_as_dictionaries(squads_list):
        position = player['position']
        positions.setdefault(position,[])
        positions[position].append(player)
    return positions
        
    

