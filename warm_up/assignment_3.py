def transform_multiple_users_to_dicts(multiple_users):
    
    users_dictionary = []
    
    for user in multiple_users:
        
        users_dictionary.append({
            "name": user[0],
            "email": user[1],
            "age": user[2],
        })
        
    return users_dictionary