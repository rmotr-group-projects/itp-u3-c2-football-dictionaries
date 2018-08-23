def group_users_by_email_domain(users):
    results = {}
    for user in users:
        domain = user['email'].split('@')[1]
        results.setdefault(domain, [])
        results[domain].append(user)
    return results
