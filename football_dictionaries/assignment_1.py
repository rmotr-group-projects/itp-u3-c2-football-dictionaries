#from squads_data import SQUADS_DATA

def players_as_dictionaries(squads_list):
    #list converted to dictionaries
    list_categories = ['number','position','name','date_of_birth','caps','club','country','club_country','year']
    
    list_of_squad_dictionaries = []
    
    for one_player in squads_list:
        #zip two lists together (combine at same index)
        single_player_dictionary = dict(zip(list_categories,one_player))

        #append a list with this data
        list_of_squad_dictionaries.append(single_player_dictionary)
    
    return list_of_squad_dictionaries

#DEBUG code
#print(players_as_dictionaries(SQUADS_DATA))