def players_by_position(data):
    position_player = {}
    playersdict = players_as_dictionaries(data)
    for player in playersdict:
        position = player['position']
        
        position_player.setdefault(position,[])
        position_player[position].append(player)
        
    return position_player

# result2 = players_by_position(SQUADS_DATA)
# goalkeepers = result2['GK']
# print(len(goalkeepers))

# print(result2)

# midfielders = result2['MF']


# print(result2)
