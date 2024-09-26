
def players_by_country_and_position(squads_list):
    # result = {'argentina' : {'GK' : [{sqaud}], 'MF' : [{squad}], 'FW' : [{squad}]} } it is a dictionary with the values being dictionaries whose values are lists of dictionaries.
    result = {}
    for squad in squads_list:
        country = squad[6]
        result.setdefault(country, {})
        position = squad[1]
        result[country].setdefault(position, [])
        insidedict = {
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
        result[country][position].append(insidedict)
    return result 
    
    
#OLD SOLUTION THAT IS WAY TOO COMPLICATED BUT PASSES TESTS  
# from football_dictionaries.assignment_1 import players_as_dictionaries   
#    result = {
#        'Argentina' : {},
#        'Belgium' : {},
#        'Brazil' : {},
#        'South Korea' : {}
#    }
#    data = players_as_dictionaries(squads_list)
#    for squad in data:
#        if squad['position'] == 'GK':
#            if squad['country'] == 'Argentina':
#                result['Argentina'].setdefault('GK', [])
#                result['Argentina']['GK'].append(squad)
#            if squad['country'] == 'Belgium': 
#                result['Belgium'].setdefault('GK', [])
#                result['Belgium']['GK'].append(squad)
#            if squad['country'] == 'Brazil':
#                result['Brazil'].setdefault('GK', [])
#                result['Brazil']['GK'].append(squad)
#            if squad['country'] == 'South Korea':
#                result['South Korea'].setdefault('GK', [])
#                result['South Korea']['GK'].append(squad)
#        if squad['position'] == 'FW':
#            if squad['country'] == 'Argentina':
#                result['Argentina'].setdefault('FW', [])
#                result['Argentina']['FW'].append(squad)
#            if squad['country'] == 'Belgium': 
#                result['Belgium'].setdefault('FW', [])
#                result['Belgium']['FW'].append(squad)
#            if squad['country'] == 'Brazil':
#                result['Brazil'].setdefault('FW', [])
#                result['Brazil']['FW'].append(squad)
#            if squad['country'] == 'South Korea':
#                result['South Korea'].setdefault('FW', [])
#                result['South Korea']['FW'].append(squad)
#        if squad['position'] == 'MF':
#            if squad['country'] == 'Argentina':
#                result['Argentina'].setdefault('MF', [])
#                result['Argentina']['MF'].append(squad)
#            if squad['country'] == 'Belgium':
#                result['Belgium'].setdefault('MF', [])
#                result['Belgium']['MF'].append(squad)
#            if squad['country'] == 'Brazil':
#                result['Brazil'].setdefault('MF', [])
#                result['Brazil']['MF'].append(squad)
#            if squad['country'] == 'South Korea':
#                result['South Korea'].setdefault('MF', [])
#                result['South Korea']['MF'].append(squad)
#   return result
