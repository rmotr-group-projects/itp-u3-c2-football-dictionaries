from squads_data import SQUADS_DATA
from pprint import pprint


def players_by_position(squads_list):

    result = {}
    
    for item in squads_list:
        result_dict = {}
        
        # assign var to squadlist values
        number = item[0]
        position = item[1]
        name = item[2]
        dob = item[3]
        caps = item[4]
        club = item[5]
        country = item[6]
        club_country = item[7]
        year = item[8]
        
        
        # set var to dict value
        result_dict['number'] = number
        result_dict['position'] = position
        result_dict['name'] = name
        result_dict['dob'] = dob
        result_dict['caps'] = caps
        result_dict['club'] = club
        result_dict['country'] = country
        result_dict['club_country'] = club_country
        result_dict['year'] = year
        
        
        # set dict in list result
        # result.append(result_dict)
        result.setdefault(position, [])
        result[position].append(result_dict)
    
    
    return result
    
# new_player = players_by_position(SQUADS_DATA)
# new_goalkeeper = new_player['GK']
# pprint(new_goalkeeper[0])



# def players_by_position(squads_list):
    
#     players = {
#         'GK': [],
#         'MF': [],
#         'FW': []
    
#     }

#     for player_as_list in squads_list:
#         player = transform_list_player_to_dict(player_as_list)
#         position = player['position']
        
#         #players[position].append(player)
        
#         list_by_position = players.get(position)
#         list_by_position.append(player)
    
#     return players
        
        
