""" 
Matpotlib  useful for making plots

plt.plot('xlabel' , 'ylabel')
plt.plot('xlabel' , 'ylabel' , 'r') => represent red colour
'+'symbolise + sgin instead of dots
so ,  plt.plot('xlabel' , 'ylabel' , 'r+') => tells red with '+' sgin
note these + or eny else point is not continuous it is evenly placed
similarly 'g.' means green and evenly dotted
'rx' means red and 'x'


dotted plot=> by adding '-' sgin at end like , plt.plot('xlabel' , 'ylabel' , 'r+-')


plt.show()


plt.xlabel("Name x axis")
plt.ylabel("Name y axis")
plt.title("Name a plot")


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])

The first two numbers [0, 0] represent the position of the lower-left corner of the axes within the figure, where (0, 0) corresponds to the bottom-left corner of the figure.
The next two numbers [1, 1] represent the width and height of the axes, where 1 corresponds to the entire width or height of the figure.


matplotlib.pyplot.pie(data, explode=None, labels=None, colors=None, autopct=None, shadow=False)
Parameters: 
data represents the array of data values to be plotted, the fractional area of each slice is represented by data/sum(data). If sum(data)<1, then the data values returns the fractional area directly, thus resulting pie will have empty wedge of size 1-sum(data). 
labels is a list of sequence of strings which sets the label of each wedge. 
color attribute is used to provide color to the wedges. 
autopct is a string used to label the wedge with their numerical value. 
shadow is used to create shadow of wedge. 


autopct setting 


Default: When autopct is not specified, the percentage labels are not shown by default.

'%1.1f%%': This format string specifies that the percentage will be displayed with one decimal place. For example, if a wedge represents 25% of the total, it will be labeled as "25.0%".

'%d%%': This format string specifies that the percentage will be displayed as an integer, without any decimal places. For example, if a wedge represents 25% of the total, it will be labeled as "25%".

'%1.2f%%': This format string specifies that the percentage will be displayed with two decimal places. For example, if a wedge represents 25% of the total, it will be labeled as "25.00%".






Syntax: matplotlib.pyplot.scatter(x_axis_data, y_axis_data, s=None, c=None, marker=None, cmap=None, vmin=None, vmax=None, alpha=None, linewidths=None, edgecolors=None)


Parameters:

x_axis_data: An array containing data for the x-axis.matplotlib
s: Marker size, which can be a scalar or an array of size equal to the size of x or y.
c: Color of the sequence of colors for markers.
marker: Marker style.
cmap: Colormap name.
linewidths: Width of the marker border.
edgecolor: Marker border color.
alpha: Blending value, ranging between 0 (transparent) and 1 (opaque).






Normally to show mostly it is used -> plt.show()

"""

from cProfile import label
import matplotlib.pyplot as plt


import numpy as np
"""
# x = np.linspace(0,10,100) # we get evenly placed value where 0 to 100 specified


# y = np.sin(x) # this given sin value in when sin x asked
# plt.plot(x ,np.cos(x) ) # cosing graph



# plt.plot(x,y)
# plt.xlabel('Angle')
# plt.ylabel('Sine value')
# plt.title('Sine wave')
# plt.show()
"""


""""#ploting parabola
x = np.linspace(0,5,200)
y = x**2  - 5*x + 6
plt.plot(x,y , 'b.')
plt.show()

"""

"""#ploting two graphs
x = np.linspace(-5 , 5 ,50)
plt.plot(x , np.sin(x) , 'g.-')
plt.plot(x , np.cos(x) , 'r')
plt.show()


"""


"""
# making bar graphs
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
languages = [ "Hindi" , "Sanskrit", "Bagheli" , "English" , "Bengali"]
peple = [2 , 5 ,4 , 1 , 3]
ax.bar(languages,peple)
plt.xlabel('Languages')
plt.ylabel('No. of people')
plt.show() """

""" 
# making pie  chart
fig  = plt.figure()
ax = fig.add_axes([0,0,1,1])
languages = [ "Hindi" , "Sanskrit", "Bagheli" , "English" , "Bengali"]
people = [2 , 5 ,4 , 1 , 3]
ax.pie(people , labels = languages, autopct = '%1.1f%%' )
plt.show() """


""" # scatter plot

x  = np.linspace(0,10 ,20)


y = np.sin(x)
z = np.cos(x)


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])

ax.scatter(x,y,color='g')
ax.scatter(x,z,color='b')
plt.show()


 """
 
 # 3d scatter plot


""" 
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = 20 * np.random.random(100)
y = np.sin(x)
z = np.cos(x)

ax.scatter(x, y, z, c=x, cmap='Blues')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
"""















