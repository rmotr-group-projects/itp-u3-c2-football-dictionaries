def players_by_position(squads_list):

    player_list={}
    result={}
    
    for player in squads_list:
        result = players_as_dictionaries(player)
        position = result['position']
        player_list.setdefault(position, [])
        player_list[position].append(result)
    return player_list

def players_as_dictionaries(squad):
    player={
            'caps': squad[4],
            'club': squad[5],
            'club_country': squad[7],
            'country':  squad[6],
            'date_of_birth':  squad[3],
            'name':  squad[2],
            'number':  squad[0],
            'position':  squad[1],
            'year':  squad[-1]
        }
    return player