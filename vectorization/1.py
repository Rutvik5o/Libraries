list1 = [1,2,3]
list2 = [4,5,6]

result = [ x+y for x,y in zip(list1,list2)]

print(result)

#but its slow if large data