def players_by_country_and_position(squads_list):
    pass

def test_function(squads_list):
  position_dict = {'GK': [], 'DF': [], 'MF': [], 'FW': []}
  positions = ['GK', 'DF', 'MF', 'FW']
  key_list = ['number', 'position', 'name', 'date_of_birth', 'caps', 'club', 'country', 'club_country', 'year']
  master_list = []
  country_list = []
  
  for each_list in squads_list:     # create a list of all the countries in the data
    country_list.append(each_list[6])
    country_set = set(country_list)  # change the list to a set to get unique countries
  # return country_set >> {'Japan', 'Argentina'}
 
  country_dict = {}
  for country in country_set:     # turn unique countries into keys of a dictionary
    country_dict[country] = {}
  # return country_dict >> {'Argentina': {}, 'Japan': {}}

  for each_list in squads_list:     #first for loop similar to assignment 1 - creating a list with each player as a dictionary
    each_dict= dict(zip(key_list, each_list))
    master_list.append(each_dict)
  for player in master_list:      #second for loop is iterating through each position to check if the position is in each player dictionary in the list from asgmt 1
    for position in positions:
      if player['position'] == position:
        position_dict[position].append(player)
  return position_dict    #Assignment 2 output 
  
  '''technically all that is left is to search the assignment 2 output for the country and then insert the matches into the country_dict to the applicable country_key'''
  
  # ============================================================================ #
''' Santiagos solution ''' 
def players_by_country_and_position(squads_list):
    squad = players_as_dictionaries(squads_list)
    by_country = {}

    for player in squad:
        country = player['country']
        position = player['position']
        by_country.setdefault(country, {})
        by_country[country].setdefault(position, [])
        by_country[country][position].append(player)

    return by_country