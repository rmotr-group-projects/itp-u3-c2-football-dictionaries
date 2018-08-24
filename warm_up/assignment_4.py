from pprint import pprint

def group_users_by_email_domain(users):
    grouped_dict = {}
    
    for user in users:
        if '@' in user['email']: 
            email = user['email']
            account_type = email[email.index('@') + 1: len(email) + 1]
        grouped_dict.setdefault(account_type, []) 
        grouped_dict[account_type].append(user) 
        
    return grouped_dict

