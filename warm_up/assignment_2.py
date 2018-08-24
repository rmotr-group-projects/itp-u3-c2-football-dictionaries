def transform_user_list_to_dict(a_user): #receives a list of users
    name, email, age = a_user  
    
    user_dict = {
        'name': name, 
        'email': email, 
        'age': age,
    }
    return user_dict
    

