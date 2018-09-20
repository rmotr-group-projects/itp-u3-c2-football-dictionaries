def players_by_country_and_position(squads_list):
    country = {}
    holder = {}
    for player in squads_list:
        pos = player[1]
        cntry = player[6]
        if not cntry in country.keys():
            holder[cntry] = {}
            country[cntry] = []
        if not pos in country[cntry]:
            holder[cntry][pos] = []
            country[cntry].append(pos)
        holder[cntry][pos].append({'number':player[0],'position':player[1],'name':player[2],'date_of_birth':player[3],'caps':player[4],'club':player[5],'country':player[6],'club_country':player[7],'year':player[8]})
    return holder
