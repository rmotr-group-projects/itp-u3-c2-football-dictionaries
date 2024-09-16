from football_dictionaries.assignment_2 import players_by_position
from football_dictionaries.assignment_2 import get_player_position
from football_dictionaries.assignment_1 import transform_single_list_to_dic


def get_country_of_player(player_list):
    return player_list[6]

def get_country_of_player_dic(player_dic):
    return player_dic['country']

# def players_by_country_and_position(squads_list):
#     dic_players_by_country ={}
    
#     for player in squads_list:
#         country = get_country_of_player(player)
#         position = get_player_position(player)
#         dic_players_by_country.setdefault(country,{})
#         player_dic = transform_single_list_to_dic(player)
#         dic_players_by_country[country][position].append(player_dic)
        
#     return dic_players_by_country

def players_by_country_and_position(squads_list):
    dic_players_by_country ={}
    
    for player in squads_list:
        country = get_country_of_player(player)
        position = get_player_position(player)
        dic_players_by_country.setdefault(country,{})
        player_dic = transform_single_list_to_dic(player)
        dic_players_by_country[country].setdefault(position,[])
        dic_players_by_country[country][position].append(player_dic)
        
    return dic_players_by_country


