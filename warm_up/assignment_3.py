def transform_multiple_users_to_dicts(multiple_users):
    
    final_list = []
    
    for user in multiple_users: #this will loop through each list in multiple_users for me. Each user is a LIST.
        user_dict = {}
        
        for index, item in enumerate(user): #checking index of the user list and assigning it to the appropriate key depending on what index is.
            
            if index == 0:
                user_dict["name"] = item
            if index == 1:
                user_dict["email"] = item
            if index == 2:
                user_dict["age"] = item
        
        final_list.append(user_dict)
        
    return final_list
            
