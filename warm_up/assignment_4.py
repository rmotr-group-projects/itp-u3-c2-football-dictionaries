def group_users_by_email_domain(users):
    
    users_grouped = {}
    
    for user in users:
        
        email_domain = user['email'].split('@')[-1]
        
        if email_domain in users_grouped:
            users_grouped[email_domain].append(user)
        else:
            users_grouped[email_domain] = [user]
            
    return users_grouped
            
        
        
