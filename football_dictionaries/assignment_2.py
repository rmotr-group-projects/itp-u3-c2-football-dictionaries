def players_as_dictionaries(players):
    retArr=[]
    for player in players:
            retArr.append({
            'number': player[0],
            'position': player[1],
            'name': player[2],
            'date_of_birth': player[3],
            'caps': player[4],
            'club': player[5],
            'country': player[6],
            'club_country': player[7],
            'year': player[8],
            })
    return retArr

def players_by_position(squad_data):
    squad = players_as_dictionaries(squad_data)
    arr = {}
    for person in squad:
        if person['position'] not in arr:
            arr[person['position']]=[person]
        else:
            arr[person['position']].append(person)
    return arr
