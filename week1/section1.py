#broadcasting
#  import numpy as np
# a = np.array([ 1 , 2 , 3])

# b = np.array([ [ 1  , 10  , 100 ],
#             [ 20 , 200 , 2000] ])

# c = a + b
# print(c)




# np.dot && np.matul
# import numpy as np
# arr1 = np.array([ 1 , 5 , 10])

# arr2 = np.array([10 , 20, 30])

# c = np.dot(arr1 , arr2)
# print(c)
# c2 = np.matmul(arr1 , arr2)
# print(c2)



# import numpy as np
# arr1 = np.array([[ 1 , 5 , 10],
#                 [10 , 100 , 1000]])

# arr2 = np.array([[1 , 5, 10],
#                 [10 , 100 , 1000]])

# c = np.dot(arr1 , arr2.T)
# print(c)
# c2 = np.matmul(arr1 , arr2.T)
# print(c2)





# handling mixed data
# import numpy as np
# dt = np.dtype( [('name' , 'U10') , ('age' , 'i4') , ('salary' , 'f4')] )
# data = np.array([ ('asmaa' , 21 , 5000.00) ] ,dtype = dt)

# print( data['name'] )




# np.nan()
# import numpy as np
# arr = np.array( [1 , 2 , 3 , np.nan] )

# print(np.nanmean(arr))  # output = 2
# print(np.nanstd(arr))
# print(np.isnan(5))



# perform inplace modifications
# import numpy as np
# arr = np.array([1 , 2 , 3])
# sum = np.add(arr, 10, out=arr )
# print(sum)



# eigenvalue && eigenvector
# import numpy as np
# arr = np.array( [[1 , 2],
#                 [3 , 4]] )

# eigenvalue , eigenvector = np.linalg.eig(arr)
# print(f"eigenvalue: {eigenvalue}\neigenvector: {eigenvector}")





# unique values
# import numpy as np
# arr = np.array( [2 , 3 , 4 , 4 , 1 , 1] )

# unique , count = np.unique( arr , return_counts= True )

# print(f"unique numbers: {unique}\nunique count: {count}")



# random matrix
# import numpy as np
# arr = np.random.rand(3,3)

# print(arr)
# print("*****************************")
# print(arr / np.sum(arr) *100)



# filtered mask
# import numpy as np
# arr = np.array( [20 , 40 , 60 , 100] )

# mask = arr[arr > 25]
# print(mask)




# generate dataset
import numpy as np
np.random.seed(42)

data = np.random.randint( 20 , 60 , size = (10,5) )
print(data)

median = np.median(data , axis=0)
print(f"median: {median}")

