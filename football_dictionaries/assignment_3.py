# structure = {
#   "GK": [{..player1..}, {..player2..}],
#   "DF": [{..player1..}, {..player2..}],
#   "MF": [{..player1..}, {..player2..}],
#   "FW": [{..player1..}, {..player2..}],
# }

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


dict_structure = {
    'number': "",
    'position': "",
    'name': "",
    'date_of_birth': "",
    'caps': "",
    'club': "",
    'country': "",
    'club_country': "",
    'year': "",
}

list_vars = ['number',
    'position',
    'name',
    'date_of_birth',
    'caps',
    'club',
    'country',
    'club_country',
    'year']


def players_as_dictionaries(squads_list):
    results = []
    for players in squads_list:
        y = {}
        for attributes in range(len(players)):
            y.update({list_vars[attributes]: players[attributes]})
        results.append(y)
    return results

    
def players_by_country_and_position(squads_list):
  squads_list = players_as_dictionaries(squads_list)
  listCountry = []
  resultsF = {}
  #getting a masterlist of all countries
  for player_dicts in squads_list:
      listCountry.append(player_dicts['country'])
  #removing duplicate countries
  y = set(listCountry)
  #converting back to a list
  listCountry = list(y)
  #setting a null value for each country in dict
  for country in listCountry:
      resultsF[country] = None
  #Here we will add the positions for ea country
  for country in listCountry:
      #initialze the sub-dict for each country
      citizens = {}
      #list of positions to be cleared for each loop
      listPos = []
      
      #adding a masterlist of positions for each country
      for player_dicts in squads_list:
        playerPos = []
        if player_dicts['country'] == country:
            listPos.append(player_dicts['position'])
            playerPos.append(player_dicts)
      #removing duplicate positions
      #print(playerPos)
      x = set(listPos)
      listPos = list(x)
      #modifying the sub dict to include all positions
      for pos in listPos:
          citizens[pos] = []
      resultsF[country] = citizens
  #Now to add the players to their correct positions within the master dictionary structure
  for keys, values in resultsF.items():
    for k, v in values.items():
      for player_dicts in squads_list:
        if (player_dicts['country'] == keys) and (player_dicts['position'] == k):
          v.append(player_dicts)
  
  print(resultsF)
  return resultsF    
      
      
"""I have the correct dictionary structure
now we need to loop through all the players one by one
if that player falls into a certain country AND position
we will add that player to the correct list within the dictionary
"""
      
      
      
      
      
      
  # Append players to right positions
  # for countries, posDict in resultsF.items():
  #   for player_dicts in squads_list:
  #     for position, playerList in posDict.items():
  #       miniList = []
  #       if player_dicts['country'] == countries and player_dicts['position'] == position:
  #         miniList.append(player_dicts)
  #       playerList = miniList
  # print(resultsF)
  # return resultsF
  
  
  #print(resultsF)
    
"""Need to do this sequentially
make dictionary with list of countries
loop through players and then add their respective positions
to their respective country"""



players_by_country_and_position(SQUADS_DATA)