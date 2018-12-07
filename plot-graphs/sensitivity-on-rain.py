# importing the required modules 
import matplotlib.pyplot as plt 
import numpy as np 
  
# setting the x - coordinates 
# x1 = np.arange(-1000, 1000, 0.01)
x1 = np.arange(0, 1, 0.01) 
y1 = (0.272 * x1) + (0.482 * (1-x1))

# plotting the line 1 points  
plt.plot(x1, y1, label = "No Harvest") 
  
# line 2 points 
# x1 = np.arange(-1000, 1000, 0.01)
x = np.arange(0, 1, 0.01)
y = 0.37811 + (x * 0)
# plotting the line 2 points
plt.plot(x, y, label = "Harvest") 
  
# naming the x axis 
plt.xlabel('P(Rain)') 
# naming the y axis 
plt.ylabel('u-value') 
# giving a title to my graph 
plt.title('Sensitivity on Rain') 
  
# show a legend on the plot 
plt.legend() 
  
# function to show the plot 
plt.show() 