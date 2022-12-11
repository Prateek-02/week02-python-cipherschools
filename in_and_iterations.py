user_info = {
    'name' : 'Prateek',
    'age' : 19,
    'fav_movies' : ['coco','kimi no na wa'],
    'fav_tunes' : ['awakening','fairy tail']
}

#check if key exist in dictionary
# if 'name' in user_info:
#     print('present')
# else:
#     print('not present')     

#check if value exist in dictionary
# if 'Prateek' in user_info.values():
#     print('present')
# else:
#     print('not present')     

#loops in dictionary
# for i in user_info.values():
#     print(i)

#values method
# user_values = user_info.values()
# print(user_values)
# print(type(user_values))

#keys method
# user_keys = user_info.keys()
# print(user_keys)
# print(type(user_keys))

#items method
# user_items = user_info.items()
# print(user_items)
# print(type(user_items))

for key, value in user_info.items():
    print(f"key is {key} and value is {value}")
