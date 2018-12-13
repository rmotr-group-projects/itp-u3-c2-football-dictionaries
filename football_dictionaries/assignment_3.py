from .assignment_2 import *

players_list = players_as_dictionaries(SQUADS_DATA)

def players_by_country_and_position(data):
    country_summary_dictionary = {}
    unique_country_keys = get_unique_country_keys(data)
    unique_position_keys = get_unique_position_keys(data)
    for country in unique_country_keys:
        position_summary_dictionary = {}
        for position in unique_position_keys:
            players_per_position_list = get_players_at_position_in_country(data, position, country)
            if players_per_position_list != [] and players_per_position_list != None:
                position_summary_dictionary[position] = players_per_position_list
        country_summary_dictionary[country] =  position_summary_dictionary
    return country_summary_dictionary


def get_players_at_position_in_country(data, position, country):
    result = []
    for player in players_list:
        #result.setdefault(player['position'], default=None)
        if player['position'] == position and player['country'] == country:
            result.append(player)
    return result


def get_unique_country_keys(data):
    unique_country_keys = []
    for player in players_list:
        if player['country'] not in unique_country_keys:
            unique_country_keys.append(player['country'])
    return unique_country_keys

def get_unique_position_keys(data):
    unique_position_keys = []
    for player in players_list:
        if player['position'] not in unique_position_keys:
            unique_position_keys.append(player['position'])
    return unique_position_keys
