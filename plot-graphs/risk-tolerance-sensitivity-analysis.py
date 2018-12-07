# importing the required modules 
import matplotlib.pyplot as plt 
import numpy as np 
import math as math
  
# setting the x - coordinates 
x1 = np.arange(-0.0001, 0.0001, 0.000001)
# x1 = np.arange(0, 1, 0.01)

eeeeeee = 2.718281828

e_c = eeeeeee**(-82200*x1)
e_d = eeeeeee**(-12900*x1)
e_e = eeeeeee**(-82200*x1)
e_f = eeeeeee**(-42000*x1)
e_g = eeeeeee**(-36000*x1)
e_h = eeeeeee**(-30000*x1)

c = 0.21  * (1 - e_c)
d = 0.79  * (1 - e_d)
e = 0.286 * (1 - e_e)

f = 0.714 * (0.4 * (1-e_f))
g = 0.4   * (1 - e_g)
h = 0.2   * (1 - e_h)

a = 0.694 * (c + d)
b = 0.306 * (e + f + g + h)

u = a + b
# y1 = a + b
y1 = (np.log(1-u)) / (-1 * x1)

# plotting the line 1 points  
plt.plot(x1, y1, label = "No Harvest") 
  
# line 2 points 
x = np.arange(-0.0001, 0.0001, 0.000001)
# x = np.arange(0, 1, 0.01)
cool = 1 - eeeeeee ** (-34200 * x)
y = -1 * (np.log(1-cool)) / x
# y = 1 - eeeeeee **(-0.378 * x)
# plotting the line 2 points
plt.plot(x, y, label = "Harvest") 

plt.locator_params(nbins=4)
# plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
  
# naming the x axis 
plt.xlabel('Risk-Aversion Coefficient (1/$)') 
# naming the y axis 
plt.ylabel('Certain Equivalent ($)') 
# giving a title to my graph 
plt.title('Risk Tolerance Sensitivity Analysis') 
  
# show a legend on the plot 
plt.legend() 
  
# function to show the plot 
plt.show()