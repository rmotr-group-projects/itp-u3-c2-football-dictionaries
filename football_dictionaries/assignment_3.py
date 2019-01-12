from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_country_and_position(squads_list):
    
    country_position = {}  # declare dict for storage 
    squads_list = players_as_dictionaries(squads_list)  # must format list (again) from data
    
    for player in squads_list:             # loop thru players
        country_key = player['country']    # find the country key in the list
        position_key = player['position']  # find the postn key in the list

        country_position.setdefault(country_key, {})    # country key is parent level in dicts 
        country_position[country_key].setdefault(position_key, []) # 1st level nest is postn - default list

        country_position[country_key][position_key].append(player) # append to postn player list // append to country
    
    return country_position
