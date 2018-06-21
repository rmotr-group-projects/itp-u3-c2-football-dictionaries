from football_dictionaries.squads_data import SQUADS_DATA
from pprint import pprint

def players_as_dictionaries(squads_list):

    new_lis = []
    for squad in squads_list:
        d = {}
        i = 0
        d['number'] = squad[0]
        d['position'] = squad[1]
        d['name'] = squad[2]
        d['date_of_birth'] = squad[3]
        d['caps'] = squad[4]
        d['club'] = squad[5]
        d['country'] = squad[6]
        d['club_country'] = squad[7]
        d['year'] = squad[8]
        new_lis.append(d)
    return new_lis
            
    
'''
i = 0
for s in SQUADS_DATA:
    l = len(s)
    j = 0
    while j < l:
        pprint(s[j])
        j += 1
    i += 1
    if i > 0:
        break
'''
pprint(players_as_dictionaries(SQUADS_DATA))
        
