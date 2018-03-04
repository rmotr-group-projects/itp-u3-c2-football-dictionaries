# from squads_data import SQUADS_DATA
from assignment_1 import players_as_dictionaries
from pprint import pprint

def players_by_country_and_position(squads_list):
    # Emptry dictionary to set up for return
    expected_countries = {
        'Argentina': {
                'GK': [],
                'FW': []
        },
        'Brazil': {
                'MF': []
        },
        'Belgium': {
                'GK': [],
                'MF': []
        },
        'South Korea': {
                'FW': []
        },
    }

    # Assign parameter to new variable
    country_list = squads_list
    
    # Pass the new assigned list to dictionary function from assignment_1 and loop through
    for country in players_as_dictionaries(country_list):
        # Check for country and position
        if country['country'] == 'Argentina' and country['position'] == 'GK':
            # Append to correct country and position
            expected_countries['Argentina']['GK'].append(country)
        
        # Check for country and position
        if country['country'] == 'Argentina' and country['position'] == 'FW':
            # Append to correct country and position
            expected_countries['Argentina']['FW'].append(country)
        
        # Check for country and position
        if country['country'] == 'Brazil' and country['position'] == 'MF':
            # Append to correct country and position
            expected_countries['Brazil']['MF'].append(country)
        
        # Check for country and position
        if country['country'] == 'Belgium' and country['position'] == 'GK':
            # Append to correct country and position
            expected_countries['Belgium']['GK'].append(country)
        
        # Check for country and position
        if country['country'] == 'Belgium' and country['position'] == 'MF':
            # Append to correct country and position
            expected_countries['Belgium']['MF'].append(country)
        
        # Check for country and position
        if country['country'] == 'South Korea' and country['position'] == 'FW':
            # Append to correct country and position
            expected_countries['South Korea']['FW'].append(country)

    return expected_countries
        

#pprint(players_by_country_and_position(SQUADS_DATA))