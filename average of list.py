L=[1,3,5,7,9,8,6,4,2]
print("original list is:",L)

count=0
for i in L:
    count=count+i
    length=len(L)
avg=count/length
print("the count is",count)
print("the length of the list is",length,"characters")
print("the average of the list is",avg)
        