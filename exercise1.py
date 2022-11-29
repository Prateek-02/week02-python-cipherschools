#ask user a number like 1234
#calculate sum of digits ---> 1+2+3+4
sum = 0
n = input("enter a number : ")
for i in  range(0,len(n)):
    sum = sum + int(n[i])
print (sum)    



#ask user name and count each character

name = input("enter your name : ")
b =""
for i in range(0,len(name)):
    if name[i] not in b:
        print(f"{name[i]} : {name.count(name[i])}")
        b = b + name[i]
      