import pprint
#from squads_data import SQUADS_DATA  
from assignment_1 import players_as_dictionaries



def players_by_country_and_position(arg1):
    arg2 = players_as_dictionaries(arg1)
    
    Argentina = []
    Belgium = []
    Brazil = []
    SKorea = []
    
    for i in range(len(arg2)):
        country = arg2[i].get('country')
        
        if country == 'Argentina':
            Argentina.append(arg2[i])
            a_goalkeepers = []
            a_midfielders = []
            a_forwards = []
            for i in range(len(Argentina)):
               player_pos_a = Argentina[i].get('position')
               if player_pos_a == 'GK':
                   a_goalkeepers.append(Argentina[i])
               elif player_pos_a == 'MF':
                   a_midfielders.append(Argentina[i])
               elif player_pos_a == 'FW':
                   a_forwards.append(Argentina[i])
              
        elif country == 'Belgium':
            Belgium.append(arg2[i])
            be_goalkeepers = []
            be_midfielders = []
            be_forwards = []
            for i in range(len(Belgium)):
                player_pos_be = Belgium[i].get('position')
                if player_pos_be == 'GK':
                    be_goalkeepers.append(Belgium[i])
                elif player_pos_be == 'MF':
                    be_midfielders.append(Belgium[i])
                elif player_pos_be == 'FW':
                    be_forwards.append(Belgium[i])           
        
        elif country == 'Brazil':
            Brazil.append(arg2[i])
            br_goalkeepers = []
            br_midfielders = []
            br_forwards = []
            for i in range(len(Brazil)):
                player_pos_br = Brazil[i].get('position')
                if player_pos_br == 'GK':
                    br_goalkeepers.append(Brazil[i])
                elif player_pos_br == 'MF':
                    br_midfielders.append(Brazil[i])
                elif player_pos_br == 'FW':
                    br_forwards.append(Brazil[i])
        
        elif country == 'South Korea':
            SKorea.append(arg2[i])
            sk_goalkeepers = []
            sk_midfielders = []
            sk_forwards = []
            for i in range(len(SKorea)):
                player_pos_sk = SKorea[i].get('position')
                if player_pos_sk == 'GK':
                    sk_goalkeepers.append(SKorea[i])
                elif player_pos_sk == 'MF':
                    sk_midfielders.append(SKorea[i])
                elif player_pos_sk == 'FW':
                    sk_forwards.append(SKorea[i])
    
    arg_dict = {}
    arg_dict['GK'] = a_goalkeepers
    if a_midfielders == []:
        pass
    else:
        arg_dict['MF'] = a_midfielders
    arg_dict['FW'] = a_forwards
    
    bra_dict = {}
    if br_goalkeepers == []:
        pass
    else:
        bra_dict['GK'] = br_goalkeepers
    bra_dict['MF'] = br_midfielders
    if br_forwards == []:
        pass
    else:
        bra_dict['GK'] = br_forwards
    
    
    bel_dict = {}
    bel_dict['GK'] = be_goalkeepers
    bel_dict['MF'] = be_midfielders
    bel_dict['FW'] = be_forwards
    
    sko_dict = {}
    sko_dict['GK'] = sk_goalkeepers
    sko_dict['MF'] = sk_midfielders
    sko_dict['FW'] = sk_forwards
    
    all_country_dict = {}
    all_country_dict['Argentina'] = arg_dict
    all_country_dict['Brazil'] = bra_dict
    all_country_dict['Belgium'] = bel_dict
    all_country_dict['South Korea'] = sko_dict
    
    return all_country_dict
'''  
        if country == 'Argentina':
            Argentina.append(arg2[i])
            a_goalkeepers = []
            a_midfielders = []
            a_forwards = []
            for i in range(len(arg2)):
                player_pos = arg2[i].get('position')
                if player_pos == 'GK':
                    a_goalkeepers.append(arg2[i])
                elif player_pos == 'MF':
                    a_midfielders.append(arg2[i])
                elif player_pos == 'FW':
                    a_forwards.append(arg2[i]) 



    arg_dict = {}
    arg_dict['GK'] = a_goalkeepers
    arg_dict['MF'] = a_midfielders
    arg_dict['FW'] = a_forwards
    
    
    all_country_dict = {}
    all_country_dict['Argentina'] = arg_dict
#    all_country_dict['Belgium'] = bel_dict
    
    return all_country_dict
'''   



'''   
        
        elif country == 'Brazil':
            Brazil.append(arg1[i])
            br_goalkeepers = []
            br_midfielders = []
            br_forwards = []
            for i in range(len(arg1)):
                player_pos = arg1[i].get('position')
                if player_pos == 'GK':
                    br_goalkeepers.append(arg1[i])
                elif player_pos == 'MF':
                    br_midfielders.append(arg1[i])
                elif player_pos == 'FW':
                    br_forwards.append(arg1[i])
        elif country == 'South Korea':
            South_Korea.append(arg1[i])
    '''
#    arg_dict = {}
#    arg_dict['GK'] = a_goalkeepers
#    arg_dict['MF'] = a_midfielders
#    arg_dict['FW'] = a_forwards
   
#    bel_dict = {}
#    bel_dict['GK'] = be_goalkeepers
#    bel_dict['MF'] = be_midfielders
#    bel_dict['FW'] = be_forwards
    
#    bra_dict = {}
#    bra_dict['GK'] = br_goalkeepers
#    bra_dict['MF'] = br_midfielders
#    bra_dict['FW'] = br_forwards 
    
#    all_country_dict = {}
#    all_country_dict['Argentina'] = arg_dict
#    all_country_dict['Belgium'] = bel_dict
#    all_country_dict['Brazil'] = br_forwards
#    all_country_dict['South_Korea'] = South_Korea
    
#    return arg_dict


pp = pprint.PrettyPrinter(depth=6)
pp.pprint(players_by_country_and_position(SQUADS_DATA))