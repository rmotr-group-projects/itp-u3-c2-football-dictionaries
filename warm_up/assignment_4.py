def group_users_by_email_domain(users):
    all_domains = {}
    for user in users:
        current_domain = parse_email_domains_from_user_email(user)
        all_domains.setdefault(current_domain, [])
        all_domains[current_domain].append(user)
    return all_domains


def parse_email_domains_from_user_email(user):
    return user['email'].split("@")[1]