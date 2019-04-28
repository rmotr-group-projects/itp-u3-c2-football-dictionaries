# Assignment 2
from football_dictionaries.assignment_2 import players_by_position

def players_by_country_and_position(squads_list):
    
    sq_dict = players_by_position(squads_list)
    
    tot_result={}

    
    tot_result.setdefault('Argentina',{})
    tot_result.setdefault('Belgium',{})
    tot_result.setdefault('Brazil',{})
    tot_result.setdefault('South Korea',{})
    


    for key,value in sq_dict.items(): # key is 'FW','GK'...

        a_list=[]
        b_list=[]
        c_list=[]
        d_list=[]

        for index,elem in enumerate(value):   


            if elem['country'] == 'Argentina':   

                a_list.append(elem)       
                tot_result['Argentina'][key] = a_list

            if elem['country'] == 'Belgium':
                b_list.append(elem)         
                tot_result['Belgium'][key] = b_list

            if elem['country'] == 'Brazil':            

                c_list.append(elem)            
                tot_result['Brazil'][key] = c_list                   


            if elem['country'] == 'South Korea':

                d_list.append(elem)                      
                tot_result['South Korea'][key] = d_list
    return tot_result
        

   
  