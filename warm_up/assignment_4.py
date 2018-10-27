def group_users_by_email_domain(multiple_users):
    result={}
    
    for user in multiple_users:
        split_email=user['email'].split('@')
        domain=split_email[1]
        result.setdefault(domain,[])
        result[domain].append(user)
    
    return result