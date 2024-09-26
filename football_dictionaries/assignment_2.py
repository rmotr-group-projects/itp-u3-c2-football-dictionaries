from .assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    #positions = players_as_dictionaries(squads_list)
    positions_list = {}
    for player in players_as_dictionaries(squads_list):
            position = player['position']
            
            positions_list.setdefault(position, [])
            positions_list[position].append(player)
    
    return positions_list
        
        
        
# positions_list = {
       # position:  [
            #Player data
       # ] 
# }  
    
    
#from football_dictionaries.squads_data import SQUADS_DATA


#def players_as_dictionaries(SQUADS_DATA):
    #result = []
    #for player in SQUADS_DATA:
        #result.append({ 'caps': player[4],
                        #'club': player[-4],
                        #'club_country': player[-2],
                        #'country': player[-3],
                        #'date_of_birth': player[3],
                        #'name': player[2],
                        #'number': player[0],
                        #'position': player[1],
                        #'year': player[-1],
                   # })
    #return result