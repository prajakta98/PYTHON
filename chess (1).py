p=input("Enter position:")
no=int(p[1])
if p[0]=='A' or p[0]=='C' or p[0]=='E' or p[0]=='G':
    if no>=1 and no<9:
        if no%2==0:
            print("white")
        else:
            print("black")
    else:
        print("invalid input")
elif p[0]=='B' or p[0]=='D' or p[0]=='F' or p[0]=='H':
    if no>=1 and no<9:
        if no%2==0:
            print("black")
        else:
            print("white")
    else:
        print("invalid input")
else:
    print("Invalid input")
