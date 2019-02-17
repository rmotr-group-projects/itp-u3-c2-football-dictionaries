def players_by_country_and_position(squad_data):
    posArr = {'GK':[], 'FW':[], 'DF':[], 'MF':[]}
    arr = {}
    for person in squad_data:
        if person['country'] not in arr:
            arr[person['country']]=posArr
        if person['position']=='GK':
            arr[person['country']]['GK'].append(person)
        elif person['position']=='FW':
            arr[person['country']]['FW'].append(person)
        elif person['position']=='DF':
            arr[person['country']]['DF'].append(person)
        elif person['position']=='MF':
            arr[person['country']]['MF'].append(person)    
    return arr
