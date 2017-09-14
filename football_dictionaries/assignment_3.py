# tests passing, but it's not our code. :(

# Question is now asking to sort players and position dictionary in their 
# respective countries.

def players_by_country_and_position(squads_list):
    
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
        
    # from here on is Santiago's code from github

    by_country = {}

    for player in results:
        country = player['country']
        position = player['position']
        by_country.setdefault(country, {})
        by_country[country].setdefault(position, [])
        by_country[country][position].append(player)

    return by_country

    # end santiago's code






# #Create a new dictionary named position_results.
#     position_result = dict()
 
# #Use for loop to request string "position" and search string for player. If player is found or not use append.   

#     for player in results:
#         if player["position"] not in position_result:  
#             position_result[player['position']] = []
#         position_result[player['position']].append(player)
        



# Not working....
# #Use for loop to request string "country" and search the player's country. 
#     for player in results:
#         if player['country'] not in position_result:  
#             position_result[player['country']] = {}
            
# #Now do second condition statement if position is not found in playercountry dictionary.   
        
#         if player ['position'] not in position_result[player['country']]:
#             position_result[player['country']][player['position']] = []
#         position_result[player['country']] [player['position']].append(player)
   
#     return position_result