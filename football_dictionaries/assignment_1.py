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
    
    


# result = players_as_dictionaries(SQUADS_DATA)



# pprint(result[1])
# # print(len(result))
