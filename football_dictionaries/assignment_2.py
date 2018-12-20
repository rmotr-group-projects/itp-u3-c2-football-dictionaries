from football_dictionaries.assignment_1 import players_as_dictionaries
    

def players_by_position(squads_list):
    player_roles = {}
    player_dictionary = players_as_dictionaries(squads_list)
    for player in player_dictionary: 
        player_roles.setdefault(player['position'], [])
        player_roles[player['position']].append(player)
    return player_roles

# players in playdict
# check key for value if keys match then append to player roles
# build something to compare what player@
# return player roles as dict