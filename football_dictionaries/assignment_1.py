from football_dictionaries.squads_data import SQUADS_DATA

def players_as_dictionaries(squads_list):
    res = []
    for x in squads_list:
        res_dict = {
            "caps":x[4],
            "club":x[5],
            "club_country":x[7],
            "country":x[6],
            "date_of_birth":x[3],
            "name":x[2],
            "number":x[0],
            "position":x[1],
            "year":x[8]
        }
        
                
        res.append(res_dict)     
    return res
            

