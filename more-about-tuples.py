#looping
#tuple with one element
#tuple without ()
#tuples unpacking
#list inside tuple

mixed = (1,2,3,4.0)
#for loop in tuple
for i in mixed:
    print(i)
    
#tuple with one element
num =(1,)
words = ('word1',)
print(type(num))
print(type(words)) 

#tuple without ()
guitars = 'yamaha','baton range','tylor'
print(type(guitars))

#tuple unpacking
fruits = ('apple','mango','banana')
f1,f2,f3 = (fruits)
print(f1,f3)

#list inside tuple
cars = ('tata',['BMW','audi'])
cars[1].pop()
cars[1].append('hello')
print(cars)


#min(),max(),sum
print(min(mixed))
print(max(mixed))