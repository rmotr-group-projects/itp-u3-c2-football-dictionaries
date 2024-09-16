from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    squad = players_as_dictionaries(squads_list) ## now we have access to the list of dictionaries
    
    results = {}
    for player in squad:
        position = player['position'] # get the value of the key "position"
        results.setdefault(position, []) #return position or return default if none
        results[position].append(player)
    return results
