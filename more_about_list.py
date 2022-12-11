num = list(range(1,11))
# print(num)
# popped_item = num.pop()
# print(num)
# print(num.index(1))
def negative_list(l):
    negative= []
    for i in l:
        negative.append(-i)
    return negative
print(negative_list(num))    