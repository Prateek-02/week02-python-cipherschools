#how to create dictionaries
user = {'name': 'Prateek', 'age' : 19}
print(user)

#second method to create dictionary
user1 =dict(name = 'Prateek', age = 19)
print(user1)

#how to access data in dictionary
print(user['name'])
print(user['age'])

#creating dictionary

user_info = {
    'name' : 'Prateek',
    'age'  : 19,
    'fav_singer' : ['Arijit','Mohit','kk']
}
print(user_info['fav_singer'])


#add data to empty dictionary
user_info2 = {}
user_info2['name'] = 'Prateek'
print(user_info2)