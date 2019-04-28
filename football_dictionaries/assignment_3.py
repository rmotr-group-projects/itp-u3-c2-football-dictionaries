# Data
from football_dictionaries.squads_data import SQUADS_DATA
# Assignment 1
from football_dictionaries.assignment_1 import players_as_dictionaries

# Assignment 2
from football_dictionaries.assignment_2 import players_by_position


def players_by_country_and_position(squads_list):
    result_dict = players_as_dictionaries(squads_list)
    final_answer = {}
    
    for item in result_dict:
        position_key = item.get('position')
        country_key = item['country']
        final_answer.setdefault(country_key, {})
        final_answer[country_key].setdefault(position_key, [])
        final_answer[country_key][position_key].append(item)
        
    return final_answer
    
