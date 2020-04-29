# list1=[1,2,3,4,5]
# def appendElement(list2):
    # list2.append("hello")
    # print(list2)
# appendElement(list1)

# def addition(a,b):
    # print(a+b)
# addition(3,4)

# list1=[0,0,0,0,0]
# def max(list1):
    # for i in range(0,5):
        # list1[i]=int(input("enter a number"))
        # max=list1[0]
    # for i in range(0,5):
        # if list1[i]>max:
            # max=list1[i]
    # print(max)
# max(list1)

# listofwords=["this","is","a","list","of","words"]
# items=[word[0] for word in listofwords]
# print(items)

triplet=[(x,y,z) for x in range(1,30) for y in range(1,30) for z in range(1,30) if (x**2)+(y**2)==(z**2)]
print(triplet)