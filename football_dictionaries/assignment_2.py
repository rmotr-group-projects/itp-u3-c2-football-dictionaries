from squads_data import SQUADS_DATA
from pprint import pprint


def players_by_position(squads_list):
    result = {}
    
    # need to add the previous function (assignment_2) for below output
    # will add to this at a later time
   
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
        result_dict['date_of_birth'] = dob
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