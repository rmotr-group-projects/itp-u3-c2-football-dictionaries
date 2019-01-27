def transform_list_to_dict(squads_list):
    squads_dict = {
        'number' : squads_list[0],
        'position' : squads_list[1],
        'name' : squads_list[2],
        'date_of_birth' : squads_list[3],
        'caps' : squads_list[4],
        'club' : squads_list[5],
        'club_country' : squads_list[7],
        'country' : squads_list[6],
        'year' : squads_list[8],
    }
        
    return squads_dict

def players_as_dictionaries(squads_list):
    players_list = []
    
    for player in squads_list:
 #call above function to append the dict to a list 
        squads_dict = transform_list_to_dict(player)
        players_list.append(squads_dict)
        
    return players_list    

#from squads_data import SQUADS_DATA

#print(players_as_dictionaries(SQUADS_DATA))    


#from football_dictionaries.squads_data import SQUADS_DATA

#def players_as_dictionaries(squads_list):
 #   list_names = ['number', 'position', 'name', 'date_of_birth', 'caps', 'club', 'country', #'club_country', 'year']
 #   return [dict(zip(list_names, a_list)) for a_list in squads_list]