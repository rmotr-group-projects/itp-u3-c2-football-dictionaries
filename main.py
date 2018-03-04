# From the football_dictionaries dir look at squads_data.py that has the squad data in a list
from football_dictionaries.squads_data import SQUADS_DATA
# From the football_dictionaries dir look at assignment_1.py import the function players_as_dictionaries
from football_dictionaries.assignment_1 import players_as_dictionaries
from football_dictionaries.assignment_2 import players_by_position

from pprint import pprint


#result = players_as_dictionaries(SQUADS_DATA)
result2 = players_by_position(SQUADS_DATA)
#pprint(result)
pprint(result2)
