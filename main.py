# Data
from football_dictionaries.squads_data import SQUADS_DATA

# Assignment 1
from football_dictionaries.assignment_1 import players_as_dictionaries
# Assignment 2
from football_dictionaries.assignment_2 import players_by_position
# Assignment 3
from football_dictionaries.assignment_3 import players_by_country_and_position

# functions
from pprint import pprint


result = players_by_country_and_position(SQUADS_DATA)
pprint(result)