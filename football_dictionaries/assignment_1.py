

def players_as_dictionaries(squads_list):
    # Returns info of players of a squad into a dictionary
    overall_squad_bio = []
    player_bio_info = [
        'number',
        'position',
        'name',
        'date_of_birth',
        'caps',
        'club',
        'country',
        'club_country',
        'year'
    ]
    for player in squads_list:
        """Uses the zip function to combine player_bio_info with player info lists 
           and then turns it into a dictionary"""
        combined_lists_dict = dict(zip(player_bio_info, player))
        overall_squad_bio.append(combined_lists_dict)
    return overall_squad_bio

    
