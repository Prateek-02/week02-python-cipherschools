def common(l1, l2):
    output = []
    for i in l1:
        if i in l2:
            output.append(i)
    return output

print(common([1,2,5,8], [1,2,7,6]))        