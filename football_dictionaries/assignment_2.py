def players_by_position(squads_list):
    postions = ['GK', 'DF', 'MF', 'FW']
    keys = ['number', 'position', 'name', 'date_of_birth', 'caps', 'club', "country", 'club_country', 'year']
    #mega = []
    bigmama = {}
    stage = []  # acts as staging post & chanels the dictionary using keys


    for player in squads_list:
        newd = {}

        for j in range(0, len(postions)):


            if player[1] == postions[j]:
                for w in range(0,len(keys)):
                    newd[keys[w]]=player[w]
                stage.append(newd)

# using stage variable as a trampoline
    for q in postions:
        mega = []
        for v in stage:
            if v['position']== q:
                mega.append(v)
                bigmama[q]=mega



    return bigmama

