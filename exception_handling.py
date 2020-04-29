#try:
##write code whatever you want to do
#except<exception>:#put the possible exception here
#	print("some error")
#else:
#	print("all went well")
    
	
	
# try:
    # fh=open("example_23.txt","r")
    # fh.write("this is my text file for exception handling")
# except IOError:
	# print("some error")
# else:
	# print("all went well")


##KEYERROR
# dict1={"jan":31,"march":31,"april":30}
# try:
	# print(dict1["feb"])
# except KeyError:
	# print("key could be wrong")
# else:
	# print("all went well")

##VALUEERROR
# try:
   # int("dog")
# except ValueError:
	# print("value error is there")
# else:
	# print("all went well")


##TYPEERROR
# try:
	# print("3"+3)
# except TypeError:
	# print("Error")
# else:
	# print("no error")


##ZERODIVISIONERROR
# try:
	# val=4/0
# except ZeroDivisionError:
	# print("error")
# else:
	# print("no error")


##INDEXERROR
# try:
	# list1=[1,2,3,4,5]
	# print(list1[5])
# except IndexError:
	# print("error caught")
# else:
	# print("no error at all")


##exercise1
#write a code that uses map and lambda to divide 500 by each element in the list [-100,-50,0,50,100]. If there is some error then catch that error and  print appropriate msg
# try:
   # divide=list(map(lambda x:500/x,[-100,-50,0,50,100]))
   # print(divide)
# except ZeroDivisionError:
   # print("error caught")
# else:
   # print("no error")


##exercise2
#write a code that prints 5th element of the list[1,45,"hello",39.5]. If there is an error then understand the type of error  and handle it.
# try:
   # list1=[1,45,"hello",39.5]
   # print=list1[5]
# except IndexError:
   # print("error caught")
# else:
   # print("no error")



##exercise3
#a student wrote a code that compares a string with an int.This throws some error.Catch this error and handle it.
#try:
#	 'happy'>1
#except TypeError:
#    print("error caught")
#else:
#    print("no error")
	





