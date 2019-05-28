

from football_dictionaries.squads_data import SQUADS_DATA


def players_as_dictionaries(SQUADS_DATA):
    result = []
    for player in SQUADS_DATA:
        result.append({ 'caps': player[4],
                        'club': player[-4],
                        'club_country': player[-2],
                        'country': player[-3],
                        'date_of_birth': player[3],
                        'name': player[2],
                        'number': player[0],
                        'position': player[1],
                        'year': player[-1],
                    })
    return result

    
    #my_dict = {}

#my_dict.setdefault('some_key', 0)

#if 'some_key' not in my_dict:
    #my_dict['some_key'] = 0
    
#my_string = "klae;rai;ufiadl;jldfk;akfuaioeijorw"
#my_dict= {}

#for char in my_string:
    #my_dict.setdefault(char, 0)
    #my_dict[char] += 1

#checks to see if a key is in the dictionary and if it's not there it adds it
    #print(result)
    
   




    #result = {}
    
    #for player in squads_list:
        #player_name = squads_list[2]
        #result.setdefault(player_name, [])
        #result[player_name].append(player)
        
    #return players


