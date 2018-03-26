from squads_data import SQUADS_DATA as squads_list

new_squads_list = squads_list[:]


def players_as_dictionaries(new_squads_list):
    # This function returns info of players of a squad into a dictionary
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
    for player in new_squads_list:
        """Uses the zip method to combine 'player_bio_info' with 'player' info list 
           and then turns it into a dictionary"""
        combined_lists_dict = dict(zip(player_bio_info, player))
        overall_squad_bio.append(combined_lists_dict)
    return overall_squad_bio

    
