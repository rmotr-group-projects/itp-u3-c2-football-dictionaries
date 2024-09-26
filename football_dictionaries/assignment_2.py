# Assignment 1
from football_dictionaries.assignment_1 import players_as_dictionaries
    
    

def players_by_position(squads_list):
    
    sq_list= players_as_dictionaries(squads_list)
    
    
    tot_result = {}
    
    
    for i in sq_list:        
    
        tot_result.setdefault('GK',[])
        tot_result.setdefault('MF',[])
        tot_result.setdefault('FW',[])
        
        if i['position'] == 'GK':
            tot_result['GK'].append(i)
            
        if i['position'] == 'MF':
            tot_result['MF'].append(i)
            
        if i['position'] == 'FW':
            tot_result['FW'].append(i)
            
    return tot_result
            
            
    
    
