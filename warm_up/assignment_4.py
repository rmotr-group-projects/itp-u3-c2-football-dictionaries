      
def group_users_by_email_domain(users):
    user_dict = {}

    for user in users:
        domain = user['email'].split('@')[1]
        user_dict.setdefault(domain, [])
        user_dict[domain].append(user)
    
    return user_dict
            
        
