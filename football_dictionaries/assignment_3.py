def players_by_country_and_position(squads_list):
    postions = ['GK', 'DF', 'MF', 'FW']
    keys = ['number', 'position', 'name', 'date_of_birth', 'caps', 'club', "country", 'club_country', 'year']
    #mega = []

    stage = []
    county = []



    for player in squads_list:
        newd = {}

        for j in range(0, len(postions)):


            if player[1] == postions[j]:
                for w in range(0,len(keys)):
                    newd[keys[w]]=player[w]

                stage.append(newd)


#getting the couuntries into county variable
    for item  in stage:
        if item['country'] not in county:
            county.append(item['country'])

    grandmummy = {}

    for country in county:

        hurricane = {}

        for  q in postions:
            storm = []

            for v in stage:

                if v['position']==q and v['country']==country:

                    storm.append(v)
                    hurricane[q]=storm
                    grandmummy[country]=hurricane




    return grandmummy

