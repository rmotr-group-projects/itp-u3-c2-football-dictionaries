def players_as_dictionaries(squads_list):
    
    tot_list=[]
    
    
    
    for elem in squads_list:
        
        
        a_dict={}
        
        a_dict['caps']=elem[4] 
        a_dict['club']=elem[5]
        a_dict['club_country']=elem[7]
        a_dict['country']=elem[6]
        a_dict['date_of_birth']=elem[3]
        a_dict['name']=elem[2]
        a_dict['number']=elem[0]
        a_dict['position']=elem[1]
        a_dict['year']=elem[8]
        
        tot_list.append(a_dict)
    
    return tot_list
