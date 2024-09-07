
""" 
Sea born has some built in datasets 






sns.relplot(data = tips , x  = 'total_bill' , y = 'tip' , col = 'time' , hue = 'smoker' , style = 'smoker', size = 'size')

data: This parameter specifies the DataFrame or array-like object that contains the data to be plotted. In your case, tips is likely a DataFrame containing data about restaurant tips.

x: This parameter specifies the variable to be plotted on the x-axis. In your plot, 'total_bill' is plotted on the x-axis, which likely represents the total amount of the bill.

y: This parameter specifies the variable to be plotted on the y-axis. In your plot, 'tip' is plotted on the y-axis, which likely represents the tip amount given.

col: This parameter allows you to create multiple subplots arranged in columns, each corresponding to a unique value in the specified column of the dataset. In your plot, 'time' is specified as the column variable, so the data will be split into subplots based on the different times (e.g., lunch or dinner).

hue: This parameter allows you to color the data points based on the values of a categorical variable. In your plot, 'smoker' is specified as the hue variable, so the data points will be colored differently based on whether the customer is a smoker or not.

style: This parameter allows you to vary the markers or lines in the plot based on the values of a categorical variable. In your plot, 'smoker' is specified as the style variable, so the markers will be styled differently based on whether the customer is a smoker or not.

size: This parameter allows you to vary the size of the markers based on the values of a variable. In your plot, 'size' is specified as the size variable, so the size of the markers will vary based on another variable, which is likely related to the size of the party. 








seaborn.displot(data=None, *, x=None, y=None, hue=None, row=None, col=None, weights=None, kind='hist', rug=False, rug_kws=None, log_scale=None, legend=True, palette=None, hue_order=None, hue_norm=None, color=None, col_wrap=None, row_order=None, col_order=None, height=5, aspect=1, facet_kws=None, **kwargs)

S.No	Parameter and Description
1	x,y
Variables that are represented on the x,y axis.

2	Hue
This will produce elements with different colors. It is a grouping variable. (other than x and y)

3	Legend
Boolean values, if false it suppressed the legend from being shown in the plot.

4	Row,col
These parameters define the subsets are to be plotted.

5	Data
This parameter takes the input data structure. That is either a mapping or a sequence.

6	rug
Boolean value that if true, shows marginal ticks.

7	Kind
Corresponds to the kind of plot to be drawn. Can be hist,kde or ecdf.

8	Palette
This parameter is used to set the color tone of the mapping. It can be bright, pastel, dark etc.

9	Color
Used to specify a single color, when hue mapping is not specified.

10	Aspect
Depending on this value, the size of the plot is determined.

11	Log_scale
Sets axes scales to log and the values plotted are in log scale.


When only x is passed not y
 The default plot kind is a histogram  in displot (count vs x)

 With kind as kind  = "ecdef"  which means  empirical cumulative distribution functions
 it normally creat line function graph  (Populaton vs x) 
 
 With kind as kind  = "kde"  which means  kernel density estimation
 it normally creat line function graph  (Density vs x)
 
 You can add , kde = True too which adds overlaping kde graph with histogram
 
 
 You can create bar graph with colours by adding , multiple = "stack"
 
When only x and y passed 
 The default plot kind is a scatter plot  in bivariate(square , square type dark on more type) distribution plots  (x vs y)
  
 With kind as kind  = "kde" which greates line type graph in circle type 

 
 




representation of data in the form of a map or diagram in which data values are represented as colours. it is normally 2d rectangle where some sqares are dark some lighy

seaborn.heatmap(data, *, vmin=None, vmax=None, cmap=None, center=None, annot_kws=None, linewidths=0, linecolor=’white’, cbar=True, **kwargs)

Important Parameters:

data: 2D dataset that can be coerced into an ndarray.
vmin, vmax: Values to anchor the colormap, otherwise they are inferred from the data and other keyword arguments.
cmap: The mapping from data values to color space. [cmap = cmap]
center: The value at which to center the colormap when plotting divergent data.
annot: If True, write the data value in each cell.
fmt: String formatting code to use when adding annotations.
linewidths: Width of the lines that will divide each cell.
linecolor: Color of the lines that will divide each cell.
cbar: Whether to draw a colorbar.








rellot -> dotted graph

countplot -> bar graph

"""

import seaborn as sns 
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd

""" 
tips = sns.load_dataset('tips')

# print (tips.head())

#setting the theme for the plot

sns.set_theme()



#visualize the data 

sns.relplot(data = tips , x  = 'total_bill' , y = 'tip' , col = 'time' , hue = 'smoker' , style = 'smoker', size = 'size')
plt.show()




 """

""" #load hte irirs dataset 
iris = sns.load_dataset('iris')




print(iris.head())

#scatter plot

#scatter 1
# sns.scatterplot( x = 'sepal_length' , y = 'petal_length' , hue = 'species' , data = iris)


#scatter 2
sns.scatterplot( x = 'sepal_length', y = 'petal_width', hue ='species', data = iris)

plt.show()

 """
""" 
titanic = sns.load_dataset('titanic')

print(titanic.head())

# sns.countplot(x = 'survived' , data = titanic)
sns.barplot( x = 'sex', y = 'survived' , hue= 'class' , data = titanic)
plt.show()
 """
 

      
 
 
 
 