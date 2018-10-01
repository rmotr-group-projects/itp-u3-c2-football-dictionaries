'''
This section is code for assignment_1
'''

def players_as_dictionaries(squads_list):
    
    players_as_dict = []
    
    for player in squads_list:
        
        player_dict = {
            'number': player[0],
            'position': player[1],
            'name': player[2],
            'date_of_birth': player[3],
            'caps': player[4],
            'club': player[5],
            'country': player[6],
            'club_country': player[7],
            'year': player[8],
            
        }
        
        players_as_dict.append(player_dict)
    return players_as_dict
#-------------------------------------------------------------------------------
'''
This section is code for assignment_2
'''
def players_by_position(squads_list):
    
    '''so we want a dictionary and each key in the dictionary
    will be a list of player dictionaries
    '''
    
    # This will give me a list with each player as a dictionary
    
    players_as_dict = players_as_dictionaries(squads_list)
    
    dict_of_positions = {}
    
    for player in players_as_dict:
        
        dict_of_positions.setdefault(player['position'], [])
        
        dict_of_positions[player['position']].append(player)
        
    return dict_of_positions

'''
This section is code for assignment_3
'''

#-------------------------------------------------------------------------------
'''
For this function we need a dictionary of countries. Each country will contain
a dictionary of positions. Each position will have a list which contains
every player playing in that position as a dictionary.
'''


def players_by_country_and_position(squads_list):



  dict_of_country = {}
  players_as_dict = players_as_dictionaries(squads_list)
  dict_of_positions = players_by_position(squads_list)
    
  
    
  for player_ctry in players_as_dict:
    
    #getting dictionary of countries with empty dictionaries as values
    dict_of_country.setdefault(player_ctry['country'], {}) 
    
    #defining the inner dictionary for keys in each country dictionary
    inner_dict_of_pos = {}
    
    for position in dict_of_positions.keys():
      
      # creating inner dictionaries for positions and assigning empty lists as values to store player dictionaries later
      inner_dict_of_pos.setdefault(position, [])
      
      #This for loop loops through each player and checks if their country and position matches with the outer-most country and position keys.
      #If so, that player is added to the position-key value
      
      for player in players_as_dict:
        
        if (player['country'] == player_ctry['country']) and (player['position'] == position):
          
          inner_dict_of_pos[position].append(player)
      
      #If-statement to delete a position in a country if it contains no player (empty)
      if inner_dict_of_pos[position] == []:
        del inner_dict_of_pos[position]
    
    dict_of_country[player_ctry['country']].update(inner_dict_of_pos)
    
 
        
  return dict_of_country
    
    
    
        
        
  
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


print(players_by_country_and_position(SQUADS_DATA))
        
    
