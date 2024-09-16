from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_country_and_position(squads_list):
    
    squad = players_as_dictionaries(squads_list) ## now we have access to list_of_dict

    result = {}
    for player in squad:

        country = player['country'] #Argentina
        position = player['position'] # GK

        result.setdefault(country, {}) #"Argentina" : {}
        result[country].setdefault(position, []) #result[argentina][GK]

        result[country][position].append(player)

    return result
            
            

