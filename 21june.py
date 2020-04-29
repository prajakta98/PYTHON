#a=input("enter name 1:")
dict1={}
for i in range(0,2):
    n=input("name")
    num=int(input("num"))
    dict1[n]=num
print(dict1)
p=int(input("enter a no"))
for number in dict1.values():
    if number==p:
        n=dict1[number]
        print(n)

