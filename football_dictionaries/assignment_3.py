def players_as_dictionaries(squads_list):
    resultlist = []
    for squad in squads_list:
        playerdict = {
            'caps': squad[4],
            'club': squad[5],
            'club_country': squad[7],
            'country': squad[6],
            'date_of_birth': squad[3],
            'name': squad[2],
            'number': squad[0],
            'position': squad[1],
            'year': squad[8]
        }
        resultlist.append(playerdict)
    return resultlist
    

def players_by_position(squads_list):
    ourlist = players_as_dictionaries(squads_list)
    result_dict = {}
    for squad in ourlist:
        position = squad['position']
        result_dict.setdefault(position, [])
        result_dict[position].append(squad)
    return result_dict


def players_by_country_and_position(squads_list):
    ourlist = players_as_dictionaries(squads_list)
    result_dict = {}
    for squad in ourlist:
        position = squad['position']
        country = squad['country']
        result_dict.setdefault(country, {})
        country_dict = result_dict[country]
        country_dict.setdefault(position, [])
        country_dict[position].append(squad)
        
    return result_dict