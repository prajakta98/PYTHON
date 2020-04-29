#fo=open("example.txt","r")
#print(fo.name)
#fo.close()


#fo=open("example.txt","w")
#print(fo.name)
#fo.close()



#fo=open("example1.txt","w")
#print(fo.name)
#fo.close()



#fo=open("example.txt","w")
#fo.write("my first sentence")
#fo.close()



#exercise1
#n=input("First Name:")
#r=input("Roll No:")
#c=input("College:")
#fo=open("example.txt","w")
#fo.write("First Name:{0}\n Roll No:{1}\n College:{2}\n Thanks!".format(n,r,c))
#fo.close()


#eg
# fo=open("example.txt","r")
# str1=fo.read()
# print(str1)
# fo.close()

#eg
#fo=open("example.txt","r")
#str1=fo.read(20)
#print(str1)
#fo.close()


#eg
#fo=open("example.txt","a")
#fo.write("\nThird sentence")
#fo.close()


#eg
fo=open("example.txt","r")
list1=fo.readlines()
print(list1)
fo.close()



