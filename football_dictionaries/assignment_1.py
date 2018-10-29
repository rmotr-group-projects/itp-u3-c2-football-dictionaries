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



def players_as_dictionaries(squads_list):
    players= []
    for user in squads_list:
        player_dict=players_list_as_dict(user)
        players.append(player_dict)
    return players

