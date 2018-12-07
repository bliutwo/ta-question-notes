# importing the required modules 
import matplotlib.pyplot as plt 
import numpy as np 
  
# setting the x - coordinates 
# x1 = np.arange(-1000, 1000, 0.01)
x1 = np.arange(0, 1, 0.01) 
y1 = 0.633*x1 + 0.405 * (1 - x1)

# plotting the line 1 points  
plt.plot(x1, y1, label = "Buy Spores") 
  
# line 2 points 
# x1 = np.arange(-1000, 1000, 0.01)
x = np.arange(0, 1, 0.01)
y = np.fmax(0.378, 0.273*x + 0.482 * (1-x))
# plotting the line 2 points
plt.plot(x, y, label = "No Spores") 
  
# naming the x axis 
plt.xlabel('P(Rain)') 
# naming the y axis 
plt.ylabel('u-value') 
# giving a title to my graph 
plt.title('Sensitivity on Spores') 
  
# show a legend on the plot 
plt.legend() 
  
# function to show the plot 
plt.show() 