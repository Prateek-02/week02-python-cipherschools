# very important
# for i in range(1,21):        # i =  0 to 9
#     print(f"hello world : {i}")  #it will also print the number of "hello world"


#sum from 1 to 10

# sum = 0
# for i in range(1,11):          #value of i will be from 0 to 10, 11 will be excluded
#     sum = sum + i
# print(sum)

n = int(input("enter the number : "))
sum = 0
for i in range(1,n+1):             #value of i will be from 1 to n+1,because the last number is excluded
    sum += i
print(sum)    