#split method
#convert string to list

user_info = "Prateek,19".split(",")
print(user_info)

name,age = 'Prateek,19'.split(",")
print(name)
print(age)

#join method
#convert list to string
user_info = ['Prateek','19']
print(','.join(user_info))