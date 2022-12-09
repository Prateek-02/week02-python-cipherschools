#ordered collection if items
#you can store anything in lists int,float,string

num = [1,2,3,4]
print(num)
print(num[1])                          #it will print 2

words = ["w1","w2","w3"]
print(words)
print(words[:2])                       #it will print "w1" and "w2"

mixed =[1,2,"three",4.0,"five",None]
print(mixed)
print(mixed[-1])                       #it will print the last element

mixed[1] = "two"
print(mixed)