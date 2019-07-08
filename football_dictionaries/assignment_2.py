from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    x = players_as_dictionaries(squads_list)
    z = {}
    for pos in x:
        position = pos["position"]
        z.setdefault(position,[])
        z[position].append(pos)
    return z
        
        
        
    
    
        
    
    
            
            
        
            
            
            