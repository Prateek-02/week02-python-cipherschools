# def reverse_list(l):
#     return l[::-1]
# num = [1,2,3,4]
# print(reverse_list(num))

def reverse_list(l):
    r_list = []
    for i in range(len(l)):
        popped = l.pop()
        r_list.append(popped)
    return r_list   
num = [1,2,3,4]
print(reverse_list(num)) 