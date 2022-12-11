user_info = {
    'name' : 'Prateek',
    'age' : 19,
    'fav_movies' : ['coco','kimi no na wa'],
    'fav_tunes' : ['awakening','fairy tail'],
}

#how to add data
# user_info['fav_songs'] = ['s1','s2']
# print(user_info)

#pop method
# popped = user_info.pop('fav_tunes')
# print(f"popped item is {popped}")
# print(user_info)

#popped method
popped_item = user_info.popitem()
print(user_info)
print(popped_item)