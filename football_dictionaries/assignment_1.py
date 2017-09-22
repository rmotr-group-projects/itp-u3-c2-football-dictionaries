# tests passing with both solutions.

# linh's great solution

def players_as_dictionaries(squads_list):
    field_list = [
        'number', 
        'position', 
        'name', 
        'date_of_birth', 
        'caps', 
        'club', 
        'country', 
        'club_country', 
        'year']
    
    results = []
    
    for item in squads_list:
        results.append(dict(zip(field_list, item)))
    
    return results

# brian's less pretty solution (but it works!!!)

# def players_as_dictionaries(squads_list):
    
#     field_list = [
#         'number', 
#         'position', 
#         'name', 
#         'date_of_birth', 
#         'caps', 'club', 
#         'country', 
#         'club_country', 
#         'year']

#     results = []

#     for item in squads_list:
#         temp_dictionary = {}
#         for a, b in zip(field_list, item):
#             temp_dictionary[a] = b 
#         results.append(temp_dictionary)

#     return results