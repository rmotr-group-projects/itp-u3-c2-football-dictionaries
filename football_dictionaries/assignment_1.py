def players_as_dictionaries(squads_list):
    """{
    'number': ...,
    'position': ...,
    'name': ...,
    'date_of_birth': ...,
    'caps': ...,
    'club': ...,
    'country': ...,
    'club_country': ...,
    'year': ...,
}
"""
    # the dictionaries' keys will be these fields: 
    fields = ['number','position','name','date_of_birth','caps','club','country','club_country','year']
    
    masterlist = []                     # list of lists (of all players' stats)
    
    for player in squads_list:          # every individual player is a list
        player_dict = {}                # every player gets their own brand new dict!
        for a,b in zip(fields,player):  # zip together [fields] with [player] lists into that dict
            player_dict[a] = b
        masterlist.append(player_dict)  # add this player's dict to the master list
    return masterlist

# This is what I did (Kei) - just for means of comparison 
# this is nice! -jen -- thanks Jen, so is yours :)
def players_as_dictionaries(squads_list):
    key_list = ['number', 'position', 'name', 'date_of_birth', 'caps', 'club', 'country', 'club_country', 'year']
    final_list = []
    for each_list in squads_list:
        each_dict = dict(zip(key_list, each_list))
        final_list.append(each_dict)
    return final_list
 
 
 ''' I came up w/a slightly condensed version. Pretty much the same concept - 
 the first for loop I had to recreate the list with the dictionaries and then the second for loop searches by position and categorizes by that'''
 
 def players_as_dictionaries(squads_list)::
    dict_2 = {'GK': [], 'DF': [], 'MF': [], 'FW': []}
    positions = ['GK', 'DF', 'MF', 'FW']
    key_list = ['number', 'position', 'name', 'date_of_birth', 'caps', 'club', 'country', 'club_country', 'year']
    master_list = []
  
    for each_list in squads_list:                           # first for loop is just recreating assignment 1
        each_dict= dict(zip(key_list, each_list))
        master_list.append(each_dict)

    for player in master_list:                              # second for loop iterates through each position to check if it exists in each of the dictionaries created in the first for loop
        for position in positions:
            if player['position'] == position:
                dict_2[position].append(player)
    return dict_2     