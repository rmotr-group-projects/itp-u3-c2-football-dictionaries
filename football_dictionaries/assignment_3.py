def players_by_country_and_position(squads_list):
    result_dict = players_as_dictionaries(squads_list)
    result = {}
    for players in result_dict:
        countries = players['country']
        result.setdefault(countries,{})
        position = players['position']
        result[countries].setdefault(position,[])
        result[countries][position].append(players)
        
    return result
