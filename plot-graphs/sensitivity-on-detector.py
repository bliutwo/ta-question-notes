# importing the required modules 
import matplotlib.pyplot as plt 
import numpy as np 
  
# setting the x - coordinates 
x1 = np.arange(0, 1, 0.01)
# x1 = np.arange(0, 1, 0.01) 
p = 0.694

e = (p * x1) / (p * x1 + (1-p)*(1-x1))
f = ((1-p)*(1-x1)) / (p * x1 + (1-p)*(1-x1))
g = (p * (1 - x1)) / (p * (1-x1) + (1-p) * x1)
h = (x1 * (1-p)) / (p * (1-x1) + (1-p) * x1)


a = (p * x1 + (1-p) * (1-x1))
b = np.fmax(0.369, 0.262*e + 0.475 * f)
c = (p * (1 - x1) + (1 - p) * x1)
d = np.fmax(0.369, 0.262*g + 0.475 * h)

y1 = a * b + c * d

# plotting the line 1 points  
plt.plot(x1, y1, label = "use detector") 
  
# line 2 points 
x = np.arange(0, 1, 0.01)
# x = np.arange(0, 1, 0.01)
y = 0.37811 + (x * 0)
# plotting the line 2 points
plt.plot(x, y, label = "without detector") 
  
# naming the x axis 
plt.xlabel('Sensitivity of the Detector') 
# naming the y axis 
plt.ylabel('u-value') 
# giving a title to my graph 
plt.title('Sensitivity on Detector') 
  
# show a legend on the plot 
plt.legend() 
  
# function to show the plot 
plt.show() 