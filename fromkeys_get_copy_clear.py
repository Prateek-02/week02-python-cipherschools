# d = {'name' : 'unknown','age' : 'unknown'}

# fromkeys method
# d = dict.fromkeys(['name','age'],['unknown','unknown'])
# print(d)

#get method
d = {'name' : 'Prateek','age' : 'unknown'}
# print(d['name'])
# print(d.get('names'))           #it will print none

# if d.get('name'):
#     print('present')
# else:
#     print('not present')    


# d.clear()
# print(d)

d1 = d.copy()
print(d1)