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


def players_by_country_and_position(squad_data):
    squad = players_as_dictionaries(squad_data)
    posArr = {'GK':[], 'FW':[], 'DF':[], 'MF':[]}
    arr = {}
    for person in squad:
        if person['country'] not in arr.keys():
            arr[person['country']]={}
        if person['position'] not in arr[person['country']].keys():
            arr[person['country']][person['position']] = [person]
        else:
            arr[person['country']][person['position']].append(person)
    return arr
