#Caleb and Marcos

from squads_data import SQUADS_DATA as squad;

def players_as_dictionaries(squads_list):
      # create a list to hold each player
      l = list()
      # loop over each player (list) in the list
      for player_list in squads_list:
          # convert each player (list) in squads_list to a player (dictionary) and append it to the list object
          l.append(player_to_dict(player_list))
      return l

# create a new dictionary
# assign keys to values from the list (player)
# return the newly created dictionary
def player_to_dict(player_list):
    p = dict()
    p['number'] = player_list[0]
    p['position'] = player_list[1]
    p['name'] = player_list[2]
    p['date_of_birth'] = player_list[3]
    p['caps'] = player_list[4]
    p['club'] = player_list[5]
    p['country'] = player_list[6]
    p['club_country'] = player_list[7]
    p['year'] = player_list[8]
    return p
