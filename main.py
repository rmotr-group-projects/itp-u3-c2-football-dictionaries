from football_dictionaries.squads_data import SQUADS_DATA
from football_dictionaries.assignment_1 import players_as_dictionaries
from pprint import pprint

result = players_as_dictionaries(SQUADS_DATA)  
pprint(result)

# "SQUADS_DATA = [
#   [
#     "1",                                     # Number 0
#     "GK",                                    # Position1
#     "Juan Botasso",                          # Name 2
#     "(1908-10-23)23 October 1908 (aged 21)", # Date of Birth 3
#     "",                                      # Caps 4
#     "Quilmes",                               # Club 5
#     "Argentina",                             # Country (Players Country) 6
#     "Argentina",                             # Club Country 7
#     "1930"                                   # Year 8
#   ],""

player_as_dict = {
    'caps': player_as_list [4],
    'club': player_as_list [5],
    'club_country': player_as_list [7],
    'country': player_as_list [6],
    'date_of_birth': player_as_list [3],
    'name': player_as_list [2],
    'number': player_as_list [0],
    'position': player_as_list [1],
    'year': player_as_list [8],
}

return player_as_dict

# {
#   "GK": [{..player1..}, {..player2..}],
#   "DF": [{..player1..}, {..player2..}],
#   "MF": [{..player1..}, {..player2..}],
#   "FW": [{..player1..}, {..player2..}],
# }

# def group_users_by_email_domain(multiple_users):
#     users_dict = {}
#     for user in users:
#         domain = user['email'].split('@')[1]
#         users_dict.setdefault(domain, [])
#         users_dict[domain].append(user)
#     return users_dict
def players_by_position(squads_list):
    for player in 
