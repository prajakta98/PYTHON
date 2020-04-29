import numpy as np
a=np.array([1,2,3])
# print(type(a))
# print(a.shape)
# print(a[0],a[1],a[2])
# a[0]=5
# print(a)

##1 row 3 columns
# d=np.array([1,2,3])
# print(d.shape)

##3 rows 1 column
# d=np.array([[1],[2],[4]])
# print(d.shape)

##another example
# b=np.array([[1,2,3],[4,5,6]])
# print(b)
# print(b.shape)
# print(b[0,0],b[0,1],b[1,0])

##create numpy array from list
# list1=[[1,2,3],[3,4,5],[7,8,9]]
# c=np.array(list1)
# print(c)

##exercise:
# m=np.array([[1,2,3,4],[5,6,7,8],[3,4,5,6]])
# print(m)
# print(m.shape)
# print(m[0,1],m[1,1],m[2,1])
# for i in range(4):
   # a[i]=[m[0,i]+10]
# print(a[i])

##create an array of all zeroes
# a=np.zeros((2,2))
# print(a)
# print(type(a[0,0]))

##create an array of all ones
# b=np.ones((1,2))
# print(b)
# print(type(b[0,0]))

##create a constant array
# c=np.full((2,2),7)
# print(c)
# print(type(c[0,0]))

##exercise:
# q=np.zeros((4,3))
# print(q)
# w=np.ones((4,3))
# print(w)
# e=np.full((4,3),8.5)
# print(e)

##create identity matrix
# d=np.eye(2)
# print(d)

##create random matrix
# e=np.random.random((2,2))
# print(e)


##array slicing
a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
#print(a)
##use slicing to pull out the subarray consisting of
#b=a[:2,1:3]
#print(b)
#print(a[0,1])
#b[0,0]=77
#print(a[0,1]) #changes are made in the parent array too


##create a new array from which we will select elements
#a=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
#print(a)


##create an array of indices
#b=np.array([0,2,0,1])
#print(a[np.arange(4),b])


##mutate one element from each row of a using the indices
#a[np.arange(4),b]+=10
#print(a)

##exercise
# a=np.array([[23,34,56],[-2,-13,12],[-14,20,16]])
# b=np.array([0,1,0])
# a[np.arange(3),b]+=25
# print(a)


##boolean array indexing
# a=np.array([[1,2],[3,4],[5,6]])
# bool_idx=(a>2)
# print(bool_idx)
# print(a[bool_idx])
# print(a[a>2])


##
# x=np.array([1,2])
# print(x.dtype)
# x=np.array([1.0,2.0])
# print(x.dtype)
# x=np.array([1,2],dtype=np.int64)
# print(x.dtype)


##mathematical operations on arrays
# x=np.array([[1,2],[3,4]],dtype=np.float64)
# y=np.array([[5,6],[7,8]],dtype=np.float64)
# print(x+y) # or print(np.add(x,y))
# print(x-y)
# print(np.subtract(x,y))
# print(x*y) #or print(np.multiply(x,y))
# print(x/y) #or print(np.divide(x,y))
# print(np.sqrt(x))

##single number multiplication
# array3=np.array([[1,2],[3,4]])
# print(array3.shape)
# print(array3*4)
# print(array3/2.0)
# print(array3+2)
# print(array3-2)


##matrix multiplication
# x=np.array([[1,2],[3,4]])
# y=np.array([[5,6],[7,8]])
# print(x.dot(y)) #or print(np.dot(x,y))


##sum of rows/columns
#x=np.array([[1,2],[3,4]])
#print(np.sum(x))   #compute sum of all elements
#print(np.sum(x,axis=0)) #compute sum of each column
#print(np.sum(x,axis=1)) #compute sum of each row


##transpose of a mtrix
# x=np.array([[1,2],[3,4]])
# print(x)
# print(x.T)

#eg1
# A=np.array([[4,-2],[1,-7]])
# B=np.array([[-1,2],[6,5]])
# print("x=",((3*A)-(4*B)))

# #eg2
# A=np.array([[3,-1],[0,2]])
# print("x=",(((A.T).dot(A)-(2*A))))

# #EG3
# A=np.array([[3,0,-1],[0,1,-5],[3,17,21]])
# B=np.array([[1,2,4],[23,-14,34],[-5,-6,-7]])
# C=np.array([[-2,1,33],[-3,-7,12],[0,-2,37]])
# print("x=",(2*A.dot(B))+C)


# #eg4
# A=np.array([[10,12],[21,11]])
# B=np.array([[45,3],[13,47]])
# C=np.array([[20,19],[34,-7]])
# print("lhs=",(A.dot(B).dot(C)).T)
# print("rhs=",(C.T).dot(B.T).dot(A.T))


# #eg4

# A=np.array([[10,12],[21,11]])
# B=np.array([[45,3],[13,47]])
# C=np.array([[20,19],[34,-7]])
# print("lhs=",(A+B).T)
# print("rhs=",(A.T)+(B.T))


# #EG5

# A=np.array([[10,12],[21,11]])
# B=np.array([[45,3],[13,47]])
# C=np.array([[20,19],[34,-7]])
# print("lhs=",A.dot(B+C))
# print("rhs=",(A.dot(B))+(A.dot(C)))










