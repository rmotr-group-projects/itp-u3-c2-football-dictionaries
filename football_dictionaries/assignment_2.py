def players_by_position(squad_data):
    arr = {}
    for person in squad_data:
        if person['position'] not in arr:
            arr[person['position']]=[person]
        else:
            arr[person['position']].append(person)
    return arr
