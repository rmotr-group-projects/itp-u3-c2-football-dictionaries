from pprint import pprint

users = [{
        'name': 'John',
        'email': 'john@gmail.com',     # gmail
        'age': 31
    }, {
        'name': 'Mary',
        'email': 'mary@hotmail.com',   # hotmail
        'age': 28
    }, {
        'name': 'Rose',
        'email': 'rose@yahoo.com',     # yahoo
        'age': 30
    }, {
        'name': 'Jane',
        'email': 'jane@gmail.com',     # gmail
        'age': 25
    }, {
        'name': 'Dustin',
        'email': 'dustin@hotmail.com',  # hotmail
        'age': 35
    }]
    
    
def group_users_by_email_domain(users):
    result = {}
    emails = []
    
    for item in users:
        email = item['email']
        emails.append(email)
        
        # @gmail.com
        if '@gmail.com' in email:
            gmail = '@gmail.com'
            email = gmail
            
        # @yahoo
        if '@yahoo.com' in email:
            yahoo = '@yahoo.com'
            email = yahoo
            
        # @hotmail
        if '@hotmail.com' in email:
            hotmail = '@hotmail.com'
            email = hotmail
        
        result.setdefault(email, [])
        result[email].append(item)
    
    return(result)


group_users_by_email_domain(users)
    
    
    
    
# import itertools
# from operator import itemgetter   
    
# users = [
    
#     {'name': 'john', 'domain': '@gmail.com'}, 
#     {'name':'jane', 'domain': '@hotmail.com'}, 
#     {'name': 'mary', 'domain': '@hotmail.com'}, 
#     {'name':'dustin', 'domain': '@hotmail.com'}, 
#     {'name':'rose', 'domain': '@yahoo.com'}, 
#     {'name':'jason', 'domain': '@rmotr.com'}
    
#     ]

# def group_users_by_email_domain(users):
#   # users_grouped = grouped_users_by_email_domain(users)
#     sorted_users = sorted(users, key=itemgetter('domain'))
    
#     for key, group in itertools.groupby(sorted_users, key=lambda x:x['domain']):
#         print(sorted_users)
    
    
    #domains = {
        #'@gmail.com': @gmail.com,
        #'@hotmail.com': @hotmail.com,
        #'@yahoo.com':  @yahoo.com,
        #'@rmotr.com': @rmotr.com,
    #}
# group_users_by_email_domain(users) 