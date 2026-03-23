

# name: asmaa ahmed maryah
# ID  : 811 634 546
# Task 3 && 4



#! TASK 3
# q1;
# mean = 3;
# size = 5000;
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

samples = stats.norm.rvs(size=5000, scale=3)  

# plot histogram
plt.hist(samples, bins=50)

plt.title("Histogram of Exponential Distribution (mean = 3)")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.show()

#------------------------------------------------------------------------------------------

# q2
dataset = np.random.normal(loc=50, scale=10, size=200)

# estimate parameters
mu = np.mean(dataset)
sigma = np.std(dataset)

# create bins
bins = np.histogram_bin_edges(dataset, bins=10)

# observed frequencies
observed, _ = np.histogram(dataset, bins)

# expected frequencies based on normal distribution
expected = []
for i in range(len(bins) - 1):
    p = stats.norm.cdf(bins[i+1], mu, sigma) - stats.norm.cdf(bins[i], mu, sigma)
    expected.append(p * len(dataset))

expected = np.array(expected)

# Chi-square test
chi_stat, p_value = stats.chisquare(observed, expected)

print("Chi-square statistic:", chi_stat)
print("p-value:", p_value)

if p_value > 0.05:
    print("Fail to reject H0: data follows normal distribution")
else:
    print("Reject H0: data does not follow normal distribution")

#------------------------------------------------------------------------------------------

# # q3
data = dataset
confidence = 0.95

n = len(data)
mean = np.mean(data)
std_err = stats.sem(data)

ci = stats.t.interval(confidence, df=n-1, loc=mean, scale=std_err)

print("Mean:", mean)
print("95% Confidence Interval:", ci)


#------------------------------------------------------------------------------------------

# q4
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# time values
t = np.linspace(0, 1, 500)

# function
f = np.sin(2 * np.pi * t)

# Fourier Transform
F = fft(f)

# frequencies
freq = fftfreq(len(t), t[1] - t[0])


plt.plot(freq, np.abs(F))
plt.title("Fourier Transform of sin(2πt)")
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
plt.show()

#------------------------------------------------------------------------------------------

# # q5
from scipy import linalg
import numpy as np

A = np.array([[3, 2],
            [1, -1]])

B = np.array([18, 2])

solution = linalg.solve(A, B)

print("x =", solution[0])
print("y =", solution[1])

#------------------------------------------------------------------------------------------

# # q6
from scipy import linalg
import numpy as np

A = np.array([[4, -2],
            [1, 1]])

eigenvalues, eigenvectors = linalg.eig(A)

print("Eigenvalues:")
print(eigenvalues)

print("Eigenvectors:")
print(eigenvectors)

#------------------------------------------------------------------------------------------

# # q7
from scipy.linalg import lu
import numpy as np

B = np.array([[2, 3],
            [5, 4]])

P, L, U = lu(B)

print("P =\n", P)
print("L =\n", L)
print("U =\n", U)

#!-----------------------------------------------------------------------------------------------------------------------------------!#
#!-----------------------------------------------------------------------------------------------------------------------------------!#

#! TASK 4
# Task 1: Create a Line Chart to Show Temperature Changes

# import matplotlib.pyplot as plt

x_axis = [ 'Mo' , 'Tu' , 'We' , 'Th' , 'Fr' , 'Sa' , 'Su' ]
y_axis = [  31  ,  30  ,  30  ,  29  ,  30  ,  31  ,  30  ]

plt.plot( x_axis , y_axis , marker = '*' , linestyle = '-' , color = 'blue' , label = 'Tempreture' )

plt.xlabel( 'days' )
plt.ylabel( 'tempreture' ) 
plt.title( 'Temperature Changes' ) 
plt.legend()

plt.show()

#------------------------------------------------------------------------------------------

# Task 2: Plot a Bar Chart to Compare Sales of Different Products
import matplotlib.pyplot as plt

x_axis = [ 'laptob' , 'mobile' , 'ipad' , 'computer' , 'smart watch' ]
y_axis = [    20    ,    50    ,   15   ,    10      ,      60       ]

plt.bar( x_axis , y_axis , color = [ 'lightblue' , 'pink' , 'gray' , 'brown' , 'yellow' ] )

plt.xlabel( 'product names' )
plt.ylabel( 'number of units sold' )
plt.title( ' Compare Sales of Different Products' )
plt.legend()

plt.show()

#------------------------------------------------------------------------------------------

# Task 3: Create a Pie Chart to Show the Percentage of Students in Different Courses
import matplotlib.pyplot as plt

x_axis = [ 'Computer Science' , 'Business' , 'Engineering' , 'Arts' ]
y_axis = [       400          ,   1000     ,     600       ,   500  ]

plt.pie( y_axis , labels = x_axis , colors = [ 'lightblue' , 'pink' , 'gray' , 'brown' , 'yellow' ] )

plt.title( 'the Percentage of Students in Different Courses' )
plt.legend()
plt.show()


