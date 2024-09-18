""" 
pandas is  open source data analysis library written in Python
    It leverage the power & speed of numpy to make data analysis and preprocessing easy for data scientist
    it provides rich and highly robust data operations 
    it help to use python in csv
    useful for data processing and analysis
    it is build on top of numpy library 
    Well suited for many different 




Pandas has two types of data frames:
series (1D)-> single column or row 
dataframe (2D)-> its tabular spreadsheet (row and columns)







pandas.dataframe(dictionary) => make in excel like that helps to make work pandas 
#deafault all thing have pre indexing
note like we want to make column names self we can add attribute column = [<list>]

note -> in place of dictionary you can put lists of list where each list is as column



dataframe obejct to excel format => <dataframeObject>.to_csv(path)
no index (like auto maked )  should come => dataframeObject.to_csv(path , index=False)


head and tail
data_frane_object.head(num)  =>  return  only starting num as new data frame object
note -> num  is default




data_frame_object.describe() => return count , mean , std, min , 25% , 50%, 75% , max of numercal numbeer




to ready any csv file => pd.read_csv('file_path) 
it must be csv 

you can set header = None , if no column-names just data


Get any data cell => dataframeObject[column][index]

in pandas 1st index is 3rd row and index start from 2nd row as 0 th index
change any cell value => dataframeObject[column][index] = new_value

Not change will come in file whien you do to_csv again

to change index you can do dataframeObject.index = [index values]
you can set like string values



NOte if file contains lots of data and you tell to print that data_frame object then it will so only some data of first then ... then some of  last 


panda.Series(numpy.random.rand(34))
datatype of panda.series is <class 'pandas.core.series.Series'> only if one value in rand() , if two value then it is dataframe object


dataframeObject.dtypes() => gives just like dataframe all data types (data types of each column)

dataframeObject.columns => gives columns as for list
note now attribute like row 


soriting descending as row-> dataframeObject.sort_index(axis = 0  , ascending = False)
soriting descending as column-> dataframeObject.sort_index(axis = 1  , ascending = False)

dataframeObject.sort_value(['column1', 'column2 '])




now see these operations

dataframeObject_1 = dataframeObject_2

# now if you change dataframeObject_1 it will also changed in dataframeObject_2 , it is view of another it is in same memory loaction 

To make copy do likr this ->  
dataframeObject_1 = dataframeObject_2[:]
or dataframeObject_1 = dataframeObject_2.copy()

you can even set columns anything => dataframeObject.columns = [list]

you can even set column with any string 


dataframeObject.loc[row, column] = new_value

now if row or column not exist it creates new one

loc VS [] (normal allocation)
(remember loc is good programming )



Selecting a single column (df['A'] is same as df.loc[:, 'A'] -> selects column A)
colon(:) similarly can use in vice versa
Selecting a list of columns (df[['A', 'B', 'C']] is the same as df.loc[:, ['A', 'B', 'C']] -> selects columns A, B and C)

Slicing by rows (df[1:3] is the same as df.iloc[1:3] -> selects rows 1 and 2. Note, however, if you slice rows with loc, instead of iloc, you'll get rows 1, 2 and 3 assuming you have a RangeIndex. See details here.)
However, [] does not work in the following situations:

iloc used for helping index as 0 even when index and column are different



You can select a single row with df.loc[row_label]
You can select a list of rows with df.loc[[row_label1, row_label2]]
You can slice columns with df.loc[:, 'A':'C']

note you can even put condtion is loc like EXAMPLE -> df.loc[(df['COLUMN'] < any_value)]
df[df['COLUMN'] < any_value]

must remember condition is inside () brackets 
furtheer you can even put or and condition more 


There is command drop by which you can delete row or column

df = df.drop('column_name', axis=1)
where 1 is the axis number (0 for rows and 1 for columns.)
0 is default



Or, the drop() method accepts index/columns keywords as an alternative to specifying the axis. So we can now just do:

df = df.drop(columns=['column_nameA', 'column_nameB'])
To delete the column without having to reassign df you can do:

df.drop('column_name', axis=1, inplace=True)
Finally, to drop by column number instead of by column label, try this to delete, e.g. the 1st, 2nd and 4th columns:

df = df.drop(df.columns[[0, 1, 3]], axis=1)  # df.columns is zero-based pd.Index


inplace change directly to data file then you dont need to do assign it to any variablke fir saving , also remmember implace doest return anything


to reset the index (only of row wide , each row have have index) => df.reset_index() 
but it in deafault add one more column as index , To not add => df.reset_index(drop = True)


df[column].isnull() => gives true and false series if it is null or not

df.notnull() => work same like above just opposite

note-> notnull and isnull works opposite and both works in series and in complete dataframe both


dropna function to remove column or row on the basis of none value => DataFrame.dropna(*, axis=0, how=_NoDefault.no_default, subset =.. )

axis{0 or ‘index’, 1 or ‘columns’}, default 0
Determine if rows or columns which contain missing values are removed.
0, or ‘index’ : Drop rows which contain missing values.
1, or ‘columns’ : Drop columns which contain missing value.

Only a single axis is allowed.
how{‘any’, ‘all’}, default ‘any’
Determine if row or column is removed from DataFrame, when we have at least one NA or all NA.
‘any’ : If any NA values are present, drop that row or column.
‘all’ : If all values are NA, drop that row or column.


to duplicate drop -> DataFrame.drop_duplicates(subset=None, *, keep='first')
Return DataFrame with duplicate rows removed.

Considering certain columns (subset) is optional. Indexes, including time indexes are ignored.

Parameters:
subsetcolumn label or sequence of labels, optional
Only consider certain columns for identifying duplicates, by default use all of the columns.

keep{‘first’, ‘last’, False}, default ‘first’
Determines which duplicates (if any) to keep.

‘first’ : Drop duplicates except for the first occurrence.

‘last’ : Drop duplicates except for the last occurrence.

False : Drop all duplicates.



dataframe.rename(columns={'old_column1': 'new_column1', 'old_column2': 'new_column2',...}, inplace=True)

combined_dataframe = pd.concat([df1, df2], ignore_index=True)
// to concate df1 and df2 



dataframe.shape => return tuples as (rows,columns)

dataframe.info => gives info like no of non null object in columns memory usage datatypes from which class derived(here panda) also tells size of given dataframe

To count each item in column
dataframe['column'].value_counts(dropna = True) # drop na - for excluding none count
it count overall count


dataframe['columns].value_counts() // gives count of all unique elements 


dataframe.mean(): Calculate column means.
dataframe.corr(): Compute column correlations.
dataframe.count(): Count non-null values.
dataframe.median(): Calculate column medians.
dataframe.std(): Compute column standard deviations.
dataframe.max(): Find column maximums.
dataframe.min(): Find column minimums.





groupby function  => dataframe.groupby('column')
LIKE dataframe.groupby('column').mean()
will group all 'column' data and mean it , you can also use .sum()
here 'column' can string or column no (like index)


Note -> usaually these grouped have column have unique value 
also these things not work generally in strings

further you can use aggregate function=> dataframe.groupby('column1').agg({'Column2': ['mean' , 'max' , 'min', 'count' , 'sum'})

then  column1 and column2 will come and 'mean' , 'max' , 'min', 'count' , 'sum' are sub column of column2


The syntax for the fillna() method in pandas is:
what this function do is this fills none things like Nan_value

also it is remember that in place of dataframe there can any column 

python
Copy code
DataFrame.fillna(value=None, method=None, axis=None, inplace=False, limit=None, downcast=None)
Here's a brief explanation of the parameters:

value: Scalar, dict, Series, or DataFrame. The value to use for filling missing values.
method: {'backfill', 'bfill', 'pad', 'ffill', None}, default None. Method to use for filling missing values. If None, it fills with value.
axis: {0 or 'index', 1 or 'columns'}, default None. The axis along which to fill missing values.
inplace: bool, default False. If True, fill in place. Note: this will modify any other views on this object.
limit: int, default None. If method is specified, this is the maximum number of consecutive NaN values to forward/backward fill.
downcast: dict, default None. A dict of item->dtype of what to downcast if possible, or the string 'infer' which will try to downcast to an appropriate subtype.




<pandas_dataframe>.astype(<DataFrame>)
this is to change the data type of column or data frame 


"""
import pandas as pd 
import numpy as np
"""
dict1 = {
    "name": ['Pranjal', 'Kumar', 'Akash', 'Jogipur', 'Suman', 'Riya', 'Raj', 'Shreya'],
    "marks": [92, 34, 24, 17, 88, 76, 45, 60],
    "city": ['ran', 'del', 'kol', 'mum', 'che', 'ban', 'hyd', 'pun'],
    "state": ['UP', 'Bihar', 'Maharashtra', 'Gujarat', 'Tamil Nadu', 'Karnataka', 'Telangana', 'Punjab'],
    "hobby": ['Reading', 'Painting', 'Cooking', 'Singing', 'Dancing', 'Traveling', 'Gaming', 'Writing']
}

df = pd.DataFrame(dict1)

df.to_csv('Modules/PandaTesting/First1.csv')
df.to_csv('Modules/PandaTesting/First12.csv' , index =False)




df2 = pd.read_csv('Modules/PandaTesting/MOCK_DATA.csv')


df['name'][2] = 'Ramesh'


df.index = [i for i in range(1,9)]



must see pivot table 
pd.pivot(df , index = "index_column' , column = select_column_values__who_you_want_to_make_columns , value = value_for_column)

melt is just opposite of pivot 
pd.melt(df , id_vars = "<like_index_column>",var_name = "quarter"  ,value_name = "like_value_in_pivot")
                                now it will melt quarter1, quarter2 , and quarter3...
"""
ser = pd.Series(np.random.rand(34)) #here it is row

#np.random.rand(row , column)



# print(ser)

# print(type(ser)) #<class 'pandas.core.series.Series'>



newdatafile =pd.DataFrame(np.random.rand(334,5), index = np.arange(334))
# print(newdatafile)

# print(type(newdatafile)) #<class 'pandas.core.frame.DataFrame'>


# print(newdatafile.columns)  # RangeIndex(start=0, stop=5, step=1)


# print(newdatafile.T) # it transpose column and rows

# print((newdatafile.sort_index(axis=0 , ascending=False)).head())  # sort as rows descending
# print((newdatafile.sort_index(axis=1 , ascending=False)).head())  # sort as columns descending



# print(newdatafile.head())



# newdatafile2 = newdatafile

# newdatafile2[0][0] = 123

# print(newdatafile.head())

# print(newdatafile.loc[[0,0] , [3,3]])

# print(newdatafile.loc[(newdatafile[0] > 0.9)])


print(newdatafile.reset_index())
print(newdatafile.reset_index(drop = True))


data = {'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

# Replace values where the condition is True with a new value
df['A'] = df['A'].where(df['A'] > 3, 0)

print(df)

""" 
   A   B
0  0  10
1  0  20
2  0  30
3  4  40
4  5  50
 """
 
"""
we can even use loc as  
mail_data.loc[mail_data["Category"] == "spam" , "Category" ,] = 0 
mail_data.loc[mail_data["Category"] == "ham" , "Category" ,] = 1 """



# .values  the pandas in numpy data format 

