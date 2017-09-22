def players_by_position(squads_list):
    
    # this works! i feel like i could've shortened this.
    # also I think we'll be using this as the basis for assignment 3, so 
    # it might be worth tidying up. -jen
    
    # result is a dictionary
    # keys = positions
    # values = list of dictionaries
    # 'position' = index 1, AKA playerinfo[1], new key

# make a list of players' dictionaries (copied from assignment_1.py): 
    fields = ['number','position','name','date_of_birth','caps','club','country','club_country','year']
    masterlist = []                     # list of lists (of all players' stats)
    for player in squads_list:          # every individual player is a list
        player_dict = {}                # every player gets their own brand new dict!
        for a,b in zip(fields,player):  # zip together [fields] with [player] lists into that dict
            player_dict[a] = b
        masterlist.append(player_dict)  # add this player's dict to the master list
# now loop through list of dictionaries to sort out the positions:   
    playerspositions = {}
    for playerinfo in masterlist:
        position = playerinfo['position']
        if position in playerspositions:
            # position is already in new dictionary, just add playerinfo to current list
            playerspositions[position].append(playerinfo)
        else:   # position not in playerspositions: add key and value
            playerspositions[position] = [playerinfo]
    return playerspositions


# ============================================================================ #
 
 ''' Kei's solution - I came up w/a slightly condensed version. Pretty much the same concept - 
 the first for loop I had to recreate the list with the dictionaries and then the second for loop searches by position and categorizes by that'''
 
 def players_by_position(squads_list)::
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
    
# ============================================================================ #
''' Santiagos solution ''' 
def players_by_position(squads_list):
    squad = players_as_dictionaries(squads_list)
    by_position = {}

    for player in squad:
        position = player['position']
        by_position.setdefault(position, [])
        by_position[position].append(player)

    return by_position