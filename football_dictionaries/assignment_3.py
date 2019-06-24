from football_dictionaries.assignment_2 import players_by_position

def players_by_country_and_position(squads_list):
    positions=players_by_position(squads_list)
    a_dict={}
    for key, value in positions.items():
        player1=len(value)
        for player in range(player1):
            country=value[player]['country']
            a_dict.setdefault(country,{})
            a_dict[country].setdefault(key,[])
            a_dict[country][key].append(positions[key][player])
    return a_dict

