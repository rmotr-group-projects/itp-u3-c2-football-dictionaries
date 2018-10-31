def players_as_dictionaries(squads_list):
    new_squad = []
    for squad in squads_list:
        player = ['number','position','name','date_of_birth','caps','club','country','club_country','year']
        values = squad
        player_dict = dict(zip(player, values))
        new_squad.append(player_dict)
    return new_squad
            
        