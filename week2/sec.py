

# series
# import numpy as np
# import pandas as pd
# s1 = pd.Series( ['a', np.arange(6).reshape(2,3) , 
#                 'b', [3 , 4]] )

# print(s1)


import numpy as np
import pandas as pd
# s1 = pd.Series( ['a' , np.arange(6).reshape(2,3),
#                     'b', [1 , 5] ], index = np.arange(1,5) )

# print(s1)

s1 = pd.Series(np.arange(5,10))
print(s1)
print(s1.values)
print(s1.index)

print(s1[3])
print( s1[1 : -1 : 1] )

