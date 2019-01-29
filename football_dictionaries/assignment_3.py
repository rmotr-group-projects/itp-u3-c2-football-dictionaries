def players_by_country_and_position(squads_list):
    countries = { 'Argentina' : {}, 'Belgium' : {}, 'Brazil' : {}, 'South Korea' : {}}
    for country in countries:
        for squad in squads_list:
            if country in squad and "GK" in squad:
                countries[country].setdefault('GK', []).append({
                    'caps': squad[4],
                    'club': squad[5],
                    'club_country': squad[7],
                    'country': squad[6],
                    'date_of_birth': squad[3],
                    'name': squad[2],
                    'number': squad[0],
                    'position': squad[1],
                    'year': squad[8]
                })
            elif country in squad and "MF" in squad:
                countries[country].setdefault('MF', []).append({
                    'caps': squad[4],
                    'club': squad[5],
                    'club_country': squad[7],
                    'country': squad[6],
                    'date_of_birth': squad[3],
                    'name': squad[2],
                    'number': squad[0],
                    'position': squad[1],
                    'year': squad[8]
                })
            elif country in squad and "DF" in squad:
                countries[country].setdefault("DF", []).append({
                    'caps': squad[4],
                    'club': squad[5],
                    'club_country': squad[7],
                    'country': squad[6],
                    'date_of_birth': squad[3],
                    'name': squad[2],
                    'number': squad[0],
                    'position': squad[1],
                    'year': squad[8]
                })
            elif country in squad and "FW" in squad:
                countries[country].setdefault("FW" , []).append({
                    'caps': squad[4],
                    'club': squad[5],
                    'club_country': squad[7],
                    'country': squad[6],
                    'date_of_birth': squad[3],
                    'name': squad[2],
                    'number': squad[0],
                    'position': squad[1],
                    'year': squad[8]
                })

            
    return countries