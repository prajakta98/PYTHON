list1=[0,0,0,0,0]
for i in range(0,5):
    list1[i]=int(input("enter a number"))
print(list1)
max=list1[0]
for i in range(0,5):
    if list1[i]>max:
	    max=list1[i]
print(max)