def players_by_position(squads_list):
    # result = {goalkeepers 'GK' : [{squad}]}, midfielders 'MF' : [{sqaud}]}, forwards 'FW' : [{squad}]
    
    
    result = {}
    for squad in squads_list:
        position = squad[1]
        result.setdefault(position, [])
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
        
        result[position].append(insidedict)  
    return result



  #OLD CONVOLUTED SOLUTION THAT PASSES TESTS*  
#    result = {
#        'GK' : [],
#        'MF' : [],
#        'FW' : []
 #   }
    
  #  for squad in data:
  #      if squad['position'] == 'GK':
  #          result['GK'].append(squad)
  #      if squad['position'] == 'MF':
  #          result['MF'].append(squad)
  #      if squad['position'] == 'FW':
  #          result['FW'].append(squad)
  #  return result 
