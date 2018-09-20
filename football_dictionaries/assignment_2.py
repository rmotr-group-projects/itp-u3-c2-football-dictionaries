def players_by_position(squads_list):
    position = []
    holder = {}
    for player in squads_list:
        pos = player[1]
        if not pos in position:
            holder[pos] = []
            position.append(pos)
        holder[pos].append({'number':player[0],'position':player[1],'name':player[2],'date_of_birth':player[3],'caps':player[4],'club':player[5],'country':player[6],'club_country':player[7],'year':player[8]})
    return holder
