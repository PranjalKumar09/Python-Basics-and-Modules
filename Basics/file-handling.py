#file_object = open("file_adress" , 'mode')
file = open("virtual.txt")
print(file)#<_io.TextIOWrapper name='virtual.txt' mode='r' encoding='cp1252'>
text = file.read()
print(text)
"""r (default mode) read mode gives error when file not exist 
w write mode not gives if file exist overwrite else it creates new
a append mod
rt read in text mode (default)
rb read in binary mode
"""
file.close()

"""with open("file_address" , 'mode') as f: by this mthod not needed to close    #...

 fileobject.readline() -> return one line of file and move cursror at starting of next line
 its type is stirng
 
 write lines accept in list
 
 seek and tell in python works in file objects
 
 truncate ->  fileobject.truncate(x)
 x is only integer
 truncate only show starting character x 
 like
 f.write("hello world")
 f.truncate(3) #this only write 3 character in file 
 # only hel will write in file
 
 
 """








