def group_users_by_email_domain(users):
    result = {}
    for user in users:
        email_slice = user['email'][user['email'].index('@')+1:]
        result.setdefault(email_slice,[])
        result[email_slice].append(user)
     
    return result
