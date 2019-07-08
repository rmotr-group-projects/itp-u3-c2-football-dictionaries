from football_dictionaries.assignment_1 import players_as_dictionaries 

def players_by_country_and_position(squads_list):
    x = players_as_dictionaries(squads_list)
    z = {}
    for i in x:
        country = i["country"]
        position = i["position"]
        
        z.setdefault(country,{})
        z[country].setdefault(position,[])
        
        z[country][position].append(i)
    return z
