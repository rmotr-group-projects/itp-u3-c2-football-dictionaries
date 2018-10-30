# Test 1

assert build_user_as_dict('John', 'john@gmail.com', 31) == {
    'name': 'John',
    'email': 'john@gmail.com',
    'age': 31
}



assert build_user_as_dict('Mary', 'mary@hotmail.com', 28) == {
    'name': 'Mary',
    'email': 'mary@hotmail.com',
    'age': 28
}


# Test 2



l1 = ['John', 'john@gmail.com', 31]

assert transform_user_list_to_dict(l1) == {
    'name': 'John',
    'email': 'john@gmail.com',
    'age': 31
}

l2 = ['Mary', 'mary@hotmail.com', 28]

assert transform_user_list_to_dict(l2) == {
    'name': 'Mary',
    'email': 'mary@hotmail.com',
    'age': 28
}


# Test 3


users = [
    ['John', 'john@gmail.com', 31],
    ['Mary', 'mary@hotmail.com', 28],
    ['Rose', 'rose@yahoo.com', 30]
]

users_as_dict = transform_multiple_users_to_dicts(users)

assert users_as_dict == [{
    'name': 'John',
    'email': 'john@gmail.com',
    'age': 31
}, {
    'name': 'Mary',
    'email': 'mary@hotmail.com',
    'age': 28
}, {
    'name': 'Rose',
    'email': 'rose@yahoo.com',
    'age': 30
}]



# Test 4





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

users_grouped = group_users_by_email_domain(users)

assert users_grouped == {
    'gmail.com': [{
        'name': 'John',
        'email': 'john@gmail.com',     # gmail
        'age': 31
    }, {
        'name': 'Jane',
        'email': 'jane@gmail.com',     # gmail
        'age': 25
    }],
    'hotmail.com': [{
        'name': 'Mary',
        'email': 'mary@hotmail.com',   # hotmail
        'age': 28
    }, {
        'name': 'Dustin',
        'email': 'dustin@hotmail.com',  # hotmail
        'age': 35
    }],
    'yahoo.com': [{
        'name': 'Rose',
        'email': 'rose@yahoo.com',     # yahoo
        'age': 30
    }]
}

In [ ]:

users = [{
    'name': 'Jason',
    'email': 'jason@rmotr.com',
    'age': 61
}]
users_grouped = group_users_by_email_domain(users)

assert users_grouped == {
    'rmotr.com': [{
        'name': 'Jason',
        'email': 'jason@rmotr.com',
        'age': 61
    }]
}




