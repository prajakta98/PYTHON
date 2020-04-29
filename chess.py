p=input("Enter position:")
no=int(p[1])
list1=[1,2,3,4,5,6,7,8,9]
if p[0]=='A' or p[0]=='C' or p[0]=='E' or p[0]=='G':
    for list1[no] in range(1,9):
        if list1[no%2]==0:
            print("white")
        else:
            print("black")
            break
elif p[0]=='B' or p[0]=='D' or p[0]=='F' or p[0]=='H':
    for list1[no] in range(1,9):
        if list1[no%2]==0:
            print("black")
        else:
            print("white")
            break
else:
    print("Invalid input")