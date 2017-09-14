# tests passing

# Question is now asking to sort players in their respective positions.

def players_by_position(squads_list):
    
    field_list = [
        'number', 
        'position', 
        'name', 
        'date_of_birth', 
        'caps', 
        'club', 
        'country', 
        'club_country', 
        'year']
    
    results = []
    
    for item in squads_list:
        results.append(dict(zip(field_list, item)))

    # Create a new dictionary named position_results.
    
    position_result = dict()
 
    # Use for loop to request string "position" and search string for player. 
    # If player is found or not use append.   

    for player in results:
        if player["position"] not in position_result:  
            position_result[player['position']] = []
        position_result[player['position']].append(player)
    
    return position_result

# # Santiago's solution from github

#     by_position = {}

#     for player in results:
#         position = player['position']
#         by_position.setdefault(position, [])
#         by_position[position].append(player)

#     return by_position
