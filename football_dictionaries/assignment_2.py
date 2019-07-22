

def players_as_dictionaries(data):
    playerslist = []
    
    for player in data:
        playersdict = {
    'number': player[0],
    'position': player[1],
    'name': player[2],
    'date_of_birth': player[3],
    'caps': player[4],
    'club': player[5],
    'country': player[6],
    'club_country': player[7],
    'year': player[8],
}
        playerslist.append(playersdict)
    
    return playerslist
    
    

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
