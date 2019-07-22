from football_dictionaries.assignment_1 import players_as_dictionaries


def players_by_country_and_position(squads_list):
    squads_data = players_as_dictionaries(squads_list)
    result = {}

    
    for player in squads_data:
        country = player['country']
        position = player['position']
        result.setdefault(country, {})
        result[country].setdefault(position, [])
        result[country][position].append(player)

    return result

            
            

        
    
    
    
