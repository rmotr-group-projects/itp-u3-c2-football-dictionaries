def transform_multiple_users_to_dicts(multiple_users):
    user_list = []
    
    for user in multiple_users:
        user_d = {
            'name': user[0],
            'email': user[1],
            'age': user[2],
        }
        
        user_list.append(user_d)
        
    return user_list
        
