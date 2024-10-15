#task 1

def filter_users(data):
    result = []
    for user in data:
        id, name, age, country = user
        if age > 30 and country in ['USA', 'Canada']:
            result.append(name)  
    return result

def top_10_old(data):
    sorted_users = sorted(data, key=lambda x: x[2], reverse=True)
    return sorted_users[:10]  

def find_dups(data):
    names = {}
    dups = []
    
    for user in data:
        name = user[1]
        if name in names:
            names[name] += 1 
        else:
            names[name] = 1  
    
    for name, count in names.items():
        if count > 1:  
            dups.append(name)
    
    return dups

data = [
    (1, 'Alice', 25, 'USA'),
    (2, 'Bob', 32, 'Canada'),
    (3, 'Charlie', 40, 'UK'),
    (4, 'Alice', 31, 'Canada'),
    (5, 'Dave', 45, 'USA'),
    (6, 'Eve', 35, 'USA'),
    (7, 'Frank', 28, 'Canada'),
    (8, 'Grace', 29, 'USA'),
    (9, 'Heidi', 50, 'Canada'),
    (10, 'Ivan', 37, 'USA'),
    (11, 'Judy', 45, 'Canada')
]

filtered = filter_users(data)
print("Filtered users (USA and Canada, age > 30):", filtered)

top_10 = top_10_old(data)
print("Top 10 oldest users:", top_10)

dups = find_dups(data)
print("Duplicate names:", dups)



#task 2

def count_users(trans):
    users = set()  
    for t in trans:
        users.add(t[1])  
    return len(users)  

def highest_trans(trans):
    return max(trans, key=lambda t: t[2])  

def get_ids(trans):
    trans_ids = []
    user_ids = []
    
    for t in trans:
        if len(t) >= 2: 
            trans_ids.append(t[0])  
            user_ids.append(t[1])   
        else:
            print("Oops! Inconsistent tuple size!")  
    
    return trans_ids, user_ids  


trans = [
    (101, 1, 500.0, '2023-10-01 12:30'),
    (102, 2, 300.0, '2023-10-02 13:45'),
    (103, 3, 700.0, '2023-10-03 15:10'),
    (104, 4, 250.0, '2023-10-04 16:20'),
    (105, 2, 850.0, '2023-10-05 17:50'),
    (106, 1, 400.0, '2023-10-06 19:00')
]

unique_users = count_users(trans)
print("Total unique users:", unique_users)

highest_t = highest_trans(trans)
print("Highest transaction:", highest_t)

t_ids, u_ids = get_ids(trans)
print("Transaction IDs:", t_ids)
print("User IDs:", u_ids)


#task 3

def both_A_B(a_visitors, b_visitors):
    return a_visitors.intersection(b_visitors)

def either_A_C(a_visitors, c_visitors):
    return a_visitors.symmetric_difference(c_visitors)

def update_A(a_visitors, new_visitors):
    a_visitors.update(new_visitors)

def remove_B(b_visitors, remove_visitors):
    b_visitors.difference_update(remove_visitors)

a_visitors = {1, 2, 3, 4, 5}
b_visitors = {3, 4, 5, 6, 7}
c_visitors = {5, 6, 7, 8, 9}

new_a_visitors = {10, 11, 3}
remove_from_b = {3, 7}

print("Users who visited both A and B:", both_A_B(a_visitors, b_visitors))
print("Users who visited either A or C, but not both:", either_A_C(a_visitors, c_visitors))

update_A(a_visitors, new_a_visitors)
print("Updated A visitors:", a_visitors)

remove_B(b_visitors, remove_from_b)
print("Updated B visitors:", b_visitors)


#TASK 4

def filter_users(feedback):
    new_dict = {user: data['rating'] for user, data in feedback.items() if data['rating'] >= 4}
    return new_dict

def top_5_users(feedback):
    sorted_dict = dict(sorted(feedback.items(), key=lambda x: x[1]['rating'], reverse=True)[:5])
    return sorted_dict

def combine_feedback(dicts):
    combined = {}
    for d in dicts:
        for user, data in d.items():
            if user in combined:
                combined[user]['rating'] = max(combined[user]['rating'], data['rating'])
                combined[user]['comments'] += " " + data['comments']
            else:
                combined[user] = data
    return combined

def high_ratings(feedback):
    return {user: data['rating'] for user, data in feedback.items() if data['rating'] > 3}

feedback1 = {
    1: {'rating': 5, 'comments': 'Great!'},
    2: {'rating': 3, 'comments': 'Okay'},
    3: {'rating': 4, 'comments': 'Good job!'}
}

feedback2 = {
    3: {'rating': 5, 'comments': ' Even better!'},
    4: {'rating': 2, 'comments': 'Not satisfied'},
    5: {'rating': 4, 'comments': 'Nice!'}
}

filtered = filter_users(feedback1)
print("Filtered users:", filtered)

top_5 = top_5_users(feedback1)
print("Top 5 users by rating:", top_5)

combined = combine_feedback([feedback1, feedback2])
print("Combined feedback:", combined)

high_rated = high_ratings(feedback1)
print("Users with rating > 3:", high_rated)
