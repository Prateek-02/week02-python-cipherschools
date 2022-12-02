#ex-1

# def last_char(name):
#     return name[-1]               #it will return the last char of name

# print(last_char("Prateek"))
 
#ex-2
# def odd_even(num):
#     if num%2==0:                   # if this condition is true then it will return even
#         return "even"              # if this condition is false the we will be automatically out of the if statement
#     return "odd"                   # and since we are not out of if statement then it will follow this return statement and return odd         
# print(odd_even(10))                #output = even
# print(odd_even(7))                 #output = odd
    
    
#ex-3
# def is_even(num):
#     if num%2==0:
#         return True
#     return False
# print(is_even(10))                   #output = True
# print(is_even(11))                   #output = 

#shortcut
# def is_even(num):
#     return num%2==0                  #if the statement is right or wrong it will give boolean value
# print(is_even(11))                   #if statemnet is right, output = "True" and if ststement is wrong, output = "False"

#ex-4
def song():
    return "Happy birthday song"
print(song())