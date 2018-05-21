def players_as_dictionaries(squads_list):
   
    keys =  ['number', 'position','name','date_of_birth','caps','club',"country",'club_country','year']
    squad = []
    
    for player in squads_list:
        newdict ={}
        for i in range(0,len(keys)):
            newdict[keys[i]]=player[i]
        squad.append(newdict)
            
                
    return squad
            
        
