def group_users_by_email_domain(users):
    
    users_group = {}
    
    for i in range(0, len(users)):
        
        email = users[i]["email"]
        email = email[email.find('@') +1:]
        
        users_group.setdefault(email, [])
        
        users_group[email].append(users[i])
    
    return users_group
