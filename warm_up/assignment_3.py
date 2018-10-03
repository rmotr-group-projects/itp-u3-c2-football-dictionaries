def transform_multiple_users_to_dicts(multiple_users):
    user_dict_list = []
    for user in multiple_users:
        user_dict = {
            'name' : user[0],
            'email' : user[1],
            'age' : user[2],
        }
        user_dict_list.append(user_dict)
    
    return user_dict_list
        
