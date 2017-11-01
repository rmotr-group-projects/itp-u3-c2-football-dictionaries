SQUADS_DATA = [
  [
    "1",
    "GK",
    "Juan Botasso",
    "(1908-10-23)23 October 1908 (aged 21)",
    "",
    "Quilmes",
    "Argentina",
    "Argentina",
    "1930"
  ],
  [
    "9",
    "FW",
    "Roberto Cherro",
    "(1907-02-23)23 February 1907 (aged 23)",
    "",
    "Boca Juniors",
    "Argentina",
    "Argentina",
    "1930"
  ],
  [
    "-",
    "MF",
    "Pierre Braine",
    "(1900-10-26)26 October 1900 (aged 29)",
    "42",
    "Royal Beerschot AC",
    "Belgium",
    "Belgium",
    "1930"
  ],
  [
    "-",
    "MF",
    "Alexis Chantraine",
    "(1901-03-16)16 March 1901 (aged 29)",
    "0",
    "Royal FC Liegeois",
    "Belgium",
    "Belgium",
    "1930"
  ],
  [
    "-",
    "GK",
    "Jean De Bie",
    "(1892-05-09)9 May 1892 (aged 38)",
    "37",
    "Royal Racing Club de Bruxelles",
    "Belgium",
    "Belgium",
    "1930"
  ],
  [
    "-",
    "MF",
    "Oscar",
    "(1991-09-09)9 September 1991 (aged 22)",
    "29",
    "Chelsea",
    "Brazil",
    "England",
    "2010"
  ],
  [
    "-",
    "MF",
    "Paulinho",
    "(1988-07-25)25 July 1988 (aged 25)",
    "25",
    "Tottenham Hotspur",
    "Brazil",
    "England",
    "2010"
  ],
  [
    "-",
    "MF",
    "Hernanes",
    "(1985-05-29)29 May 1985 (aged 29)",
    "23",
    "Internazionale",
    "Brazil",
    "Italy",
    "2014"
  ],
  [
    "-",
    "MF",
    "Luiz Gustavo",
    "(1987-07-23)23 July 1987 (aged 26)",
    "17",
    "VfL Wolfsburg",
    "Brazil",
    "Germany",
    "2014"
  ],
  [
    "-",
    "MF",
    "Fernandinho",
    "(1985-05-04)4 May 1985 (aged 29)",
    "6",
    "Manchester City",
    "Brazil",
    "England",
    "2014"
  ],
  [
    "-",
    "MF",
    "Willian",
    "(1988-08-09)9 August 1988 (aged 25)",
    "5",
    "Chelsea",
    "Brazil",
    "England",
    "2014"
  ],
  [
    "-",
    "FW",
    "Lee Keun-Ho",
    "(1985-04-11)11 April 1985 (aged 29)",
    "62",
    "Sangju Sangmu",
    "South Korea",
    "South Korea",
    "2014"
  ],
  [
    "-",
    "FW",
    "Koo Ja-Cheol",
    "(1989-02-27)27 February 1989 (aged 25)",
    "35",
    "Mainz 05",
    "South Korea",
    "Germany",
    "2014"
  ],
  [
    "-",
    "FW",
    "Kim Shin-Wook",
    "(1988-04-14)14 April 1988 (aged 26)",
    "26",
    "Ulsan Hyundai",
    "South Korea",
    "South Korea",
    "2014"
  ]
]

#turns SQUAD_DATA into a dict

def players_as_dictionaries(sq1):

    keys = [
    'number',
    'position',
    'name',
    'date_of_birth',
    'caps',
    'club',
    'country',
    'club_country',
    'year',
]
    player_list = [ ]

    for i in range(len(sq1)):
        result = list(zip(keys,sq1[i]))
        player_dict = { }
        for i in range(len(result)):
            player_dict[result[i][0]] = result[i][1] 
        player_list.append(player_dict)
    return player_list



def players_by_position(sq2):
    player_dict_from_fxn = players_as_dictionaries(sq2)
#    return player_dict_from_fxn

    goalkeepers = []
    defense = []
    midfielders = []
    forwards = []
    
    for i in range(len(player_dict_from_fxn)):
        player_pos = player_dict_from_fxn[i].get('position')
        if player_pos == 'GK':
            goalkeepers.append(player_dict_from_fxn[i])
#        elif player_pos == 'DF':
#            defense.append(player_dict_from_fxn[i])
        elif player_pos == 'MF':
            midfielders.append(player_dict_from_fxn[i])
        elif player_pos == 'FW':
            forwards.append(player_dict_from_fxn[i])
    
    all_pos_dict = {}
    all_pos_dict['GK'] = goalkeepers
#    all_pos_dict['DF'] = defense
    all_pos_dict['MF'] = midfielders
    all_pos_dict['FW'] = forwards
    
    return all_pos_dict

#print(players_by_position(SQUADS_DATA))



#TESTS

def test_assignment_2():
    result = players_by_position(SQUADS_DATA)
    assert len(result) == 3  # 3 positions

    goalkeepers = result['GK']
    assert len(goalkeepers) == 2

    assert goalkeepers[0] == {
        'caps': '',
        'club': 'Quilmes',
        'club_country': 'Argentina',
        'country': 'Argentina',
        'date_of_birth': '(1908-10-23)23 October 1908 (aged 21)',
        'name': 'Juan Botasso',
        'number': '1',
        'position': 'GK',
        'year': '1930'
    }

    midfielders = result['MF']
    assert len(midfielders) == 8
    assert midfielders[0] == {
        'caps': '42',
        'club': 'Royal Beerschot AC',
        'club_country': 'Belgium',
        'country': 'Belgium',
        'date_of_birth': '(1900-10-26)26 October 1900 (aged 29)',
        'name': 'Pierre Braine',
        'number': '-',
        'position': 'MF',
        'year': '1930'
    }

    forwards = result['FW']
    assert len(forwards) == 4

    assert forwards[0] == {
        'caps': '',
        'club': 'Boca Juniors',
        'club_country': 'Argentina',
        'country': 'Argentina',
        'date_of_birth': '(1907-02-23)23 February 1907 (aged 23)',
        'name': 'Roberto Cherro',
        'number': '9',
        'position': 'FW',
        'year': '1930'
    }

