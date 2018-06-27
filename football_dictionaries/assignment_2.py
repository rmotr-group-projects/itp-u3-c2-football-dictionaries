def players_by_position(squads_list):
    positions={}
    for i in squads_list:
        player= {
        "number" : i[0],
        "position" : i[1],
        "name" : i[2],
        "date_of_birth" : i[3],
        "caps" : i[4],
        "club" : i[5],
        "country" : i[6],
        "club_country" : i[7],
        "year" : i[8]
        }
        positions[player["position"]] = positions.get(player["position"],[])
        positions[player["position"]].append(player)
    return positions