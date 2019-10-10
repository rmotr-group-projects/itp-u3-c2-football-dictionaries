def players_list_as_dict(user):
   player_dict = {
       'caps': user[4],
       'club': user[5],
       'club_country': user[7],
       'country': user[6],
       'date_of_birth': user[3],
       'name': user[2],
       'number': user[0],
       'position': user[1],
       'year': user[8]
    }
   return player_dict


def players_by_position(squads_list):
    players_dict={}
    for player in squads_list:
        player_dict=players_list_as_dict(player)
        position=player_dict['position']
        players_dict.setdefault(position,[])
        players_dict[position].append(player_dict)
    return players_dict
    

