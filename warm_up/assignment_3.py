def transform_multiple_users_to_dicts(multiple_users):
    users_dict = []
    
    for user in multiple_users:
        name, email, age = user

        user_dict = {
            'name': name, 
            'email': email, 
            'age': age,
        }
        print(user_dict)
        users_dict.append(user_dict)
    
    return users_dict


