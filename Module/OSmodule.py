""""
mkdir-> to make  a folder just 
os.mkdir("complete_address")
if in same folder or relative to it no need to make complete address

like->
os.mkdir("data/Day")
this will only run if data folders exist then inside it Day folder will created otherwise error

to rename folder/file it will only rename/ (or move) if folder/ file exist otherwise error       os.rename(oldname or address,new_name or address) 


to list down all folders files
list_object = os.listdir("folder_Address")

to know current directory in string format-> os.getcwd()
to change current directory location like cd in cmd-> os.chidr("New Directory full or relative address")
note it will not move it but change direcotry now os.getcwd() will give new one

to move file ->
os.replace(source, desitnation)


to know all information of any file -> os.stat(file)


to delete file/folder
os.remove(file_name) #file
# FileNotFoundException if file is not found 


os.removedirs(new_folder_path) #remove folder
os.rmdir(new_folder_path) # remove one dirtecotry

# Note: But with these we cant delete folder containing folder for this we have do shutil.rmtree(path) 

"""


import os

"""if (not os.path.exists("data")): # checks whether path exist in order to create 100 folder
    os.mkdir("data") #if not create 
for i in range(0,100):
    os.mkdir("data/day{}".format(i+1)) #inside it from 1 to 100 folder by mayi 
"""
"""
# to change name of all 100 folder at once
if (os.path.exists("data")):
    for i in range(0,100):
        os.rename("data/day{}".format(i+1) , f"renamed_folder{i+1}")
        

"""
"""list_object = os.listdir("E:\\CODES\\Python")
print(list_object) #['.git', '.vscode', '2d animator.py', 'animating multiple.py', 'calculatorApp.py', 'clockProgram.py', 'cmd_run_sample.py', 'drag drop widgets .py', 'else with loops while for.py', 'enumerate.py', 'error_handling.py', 'if__main.py', 'images.jpg', 'KBC kaun_banega_carorepati.py', 'match_case.py', 'miscallaneous-2.py', 'miscallaneous.py', 'mouseevents.py', 'move image with canvas.py', 'move image with key.py', 'myimage.png', 'myimage2.png', 'OSmodule.py', 'pip.py', 'print_escape_comment.txt', 'py_to_exe.txt', 'QR_Generator.py', 'QR_Generator2.py', 'send Email (smtplib) .py', 'short_hand.py', 'snake_game.py', 'space.png', 'space2.png', 'temp,py', 'tempCodeRunnerFile.py', 'tempmodule.py', 'textedditor.py', 'tic_tac_toe.py', 'virtual.txt', '__pycache__']
"""
#print(os.getcwd())

"""
print(os.name)  #nt  or posix
print(os.sep) # \  
#in linux os.sep -> / 

print(os.walk(os.getcwd())) #<generator object walk at 0x0000021D34810320>

# ( , [] , [ ] ) , ( , [] , [ ] ) ,( , [] , [ ] ) ... 

    
for dirpaths, dirnames , filenames in os.walk(os.getcwd()):
    print(dirpaths, " , " , dirnames , " , " ,   filenames)
    """
    
# print(os.stat("match_case.py")) #os.stat_result(st_mode=33206, st_ino=281474976711287, st_dev=8809287437707642027, st_nlink=1, st_uid=0, st_gid=0, st_size=1422, st_atime=1704885030, st_mtime=1704359608, st_ctime=1704359218)


"""
current_folder = os.getcwd()
new_folder_path = os.path.join(address , folder/file in that address)
# it is use for just to join like concating adding on folder

#similarly split uses it seprate file name from complete address

current_folder = os.getcwd()
file_name = os.path.join(current_folder, "myimage.png")
print(os.path.split(file_name)) #('E:\\CODES\\Python', 'myimage.png')

#split extenstion
print(os.path.splitext(file_name)) #('E:\\CODES\\Python', '.png')

"""

current_folder = os.getcwd()
file_name = os.path.join(current_folder, "myimage.png")
print(os.path.splitext(file_name)) #('E:\\CODES\\Python', '.png')



